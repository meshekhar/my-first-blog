from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ['author', 'slug']
        fields = ('title', 'text', 'tags',)

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        exclude = ['question']
        fields = ('text',)
