__author__ = 'nicholassaunderson'


from django.conf.urls import patterns, url
from brotherhood import views
from django.http import HttpResponseRedirect, HttpResponse


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^home/', views.home, name='home'),
        )