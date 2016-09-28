from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apps/add/$', views.app_addition, name='app_addition'),
]
