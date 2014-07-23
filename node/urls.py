from django.conf.urls import patterns, url

from node import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<node_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<node_id>\w+)/$', views.detail, name='detail'),
)
