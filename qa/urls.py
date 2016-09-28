from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^questions$', views.question_list, name='question_list'),
    url(r'^questions/drafts/$', views.question_draft_list, name='question_draft_list'),
    url(r'^question/new/$', views.question_new, name='question_new'),
    url(r'^question/(?P<slug>[-\w]+)/$', views.question_detail, name='question_detail'),
    url(r'^question/(?P<slug>[-\w]+)/edit/$', views.question_edit, name='question_edit'),
    url(r'^question/(?P<slug>[-\w]+)/publish/$', views.question_publish, name='question_publish'),
    url(r'^question/(?P<slug>[-\w]+)/remove/$', views.question_remove, name='question_remove'),

    url(r'^question/(?P<slug>[-\w]+)/answer/$', views.add_answer_to_question, name='add_answer_to_question'),

    url(r'^answer/(?P<pk>\d+)/approve/$', views.answer_approve, name='answer_approve'),
    url(r'^answer/(?P<pk>\d+)/select/$', views.answer_select, name='answer_select'),
    url(r'^answer/(?P<pk>\d+)/remove/$', views.answer_remove, name='answer_remove'),

]
