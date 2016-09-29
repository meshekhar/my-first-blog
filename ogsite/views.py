from taggit.models import Tag
from django.shortcuts import render

def get_tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', {'tags': tags})
