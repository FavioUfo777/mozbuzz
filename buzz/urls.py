from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'buzz.views.index', name="index"),
    url(r'^about$', 'buzz.views.about', name="about"),
)