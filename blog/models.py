from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

import itertools

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    text = models.TextField()
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
        return ('post_detail', (),
                {
                    'slug' :self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = orig = slugify(self.title)
            for x in itertools.count(1):
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (orig, x)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey('blog.Post', related_name='comments')
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def approve(self):
        self.approved_comment = True
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
