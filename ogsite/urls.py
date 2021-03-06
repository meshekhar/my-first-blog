"""ogsite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url, patterns
from django.contrib.auth import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    url(r'', include('qa.urls')),
    url(r'', include('apps.urls')),
    url(r'^tags/$', 'ogsite.views.get_tags_list', name='taglist'),
    url(r'^tag/(?P<tag_slug>[a-zA-Z0-9-]+)/?$', 'qa.views.get_questions_by_tag'),
    url(r'^tag/(?P<tag_slug>[a-zA-Z0-9-]+)/(?P<selected_page>\d+)/?$', 'qa.views.get_questions_by_tag'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'', include('django.contrib.flatpages.urls')),
)
