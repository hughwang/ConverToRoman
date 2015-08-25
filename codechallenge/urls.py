from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from roman import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^roman/$', include('roman.urls',namespace="roman"),name='roman'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
)

