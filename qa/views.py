from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib import messages

def question_list(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'qa/question_list.html', {'questions': questions})

def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render_to_response('qa/question_detail.html',{'question': question,},
                                  context_instance=RequestContext(request))

@login_required
def question_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            form.save_m2m()
            return redirect('question_detail', slug=question.slug)
    else:
        form = QuestionForm()
    return render_to_response('qa/question_edit.html',
                              {'form': form},
                              context_instance=RequestContext(request))

@login_required
def question_edit(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            form.save_m2m()
            return redirect('question_detail', slug=question.slug)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'qa/question_edit.html', {'form': form})

@login_required
def question_draft_list(request):
    questions = Question.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'qa/question_draft_list.html', {'questions': questions})

@login_required
def question_publish(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.publish()
    return redirect('qa.views.question_detail', slug=slug)

@login_required
def question_remove(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('qa.views.question_list')

@login_required
def add_answer_to_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('qa.views.question_detail', slug=question.slug)
    else:
        form = AnswerForm()
    return render(request, 'qa/add_answer_to_question.html', {'form': form})

@login_required
def answer_approve(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.approve()
    return redirect('qa.views.question_detail', pk=answer.question.pk)

@login_required
def answer_select(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.select()
    return redirect('qa.views.question_detail', pk=answer.question.pk)

@login_required
def answer_unselect(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.unselect()
    return redirect('qa.views.question_detail', pk=answer.question.pk)

@login_required
def answer_remove(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    question_pk = answer.question.pk
    answer.delete()
    return redirect('qa.views.question_detail', pk=question_pk)
