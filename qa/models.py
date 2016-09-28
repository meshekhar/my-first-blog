from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django_comments.models import Comment # new
from taggit.managers import TaggableManager
from redactor.fields import RedactorField
import itertools

class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    text = RedactorField(verbose_name=u'Text')
    tags = TaggableManager()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @models.permalink
    def get_absolute_url(self):
        return ('question_detail', (),
                {
                    'slug' :self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = orig = slugify(self.title)
            for x in itertools.count(1):
                if not Question.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (orig, x)
        super(Question, self).save(*args, **kwargs)

class Answer(models.Model):
    author = models.ForeignKey(User)
    question = models.ForeignKey('qa.Question', related_name='answers')
    text = RedactorField(verbose_name=u'Text')
    approved_answer = models.BooleanField(default=False)
    selected_answer = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    selected_date = models.DateTimeField(blank=True, null=True)

    def approve(self):
        self.approved_answer = True
        self.published_date = timezone.now()
        self.save()

    def select(self):
        self.selected_answer = True
        self.selected_date = timezone.now()
        self.save()

    def unselect(self):
        self.selected_answer = False
        self.selected_date = null
        self.save()

    def __str__(self):
        return self.text

    def approved_answers(self):
        return self.answers.filter(approved_answer=True)

    def selected_answer(self):
        return self.answers.filter(selected_answer=True)
