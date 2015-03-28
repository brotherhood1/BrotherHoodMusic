from django.conf.urls import patterns, include, url
from django.contrib import admin
from brotherhood import urls
from django.http import HttpResponseRedirect, HttpResponse

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('brotherhood.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('brotherhood.urls')),
)
