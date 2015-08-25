from django.conf.urls import patterns, include, url

from django.contrib import admin
from roman import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^roman/$', include('roman.urls',namespace="roman"),name='roman'),
    #url(r'^result/$', views.result, name='result'),
    # not need admin for now
    #url(r'^admin/', include(admin.site.urls)),
)

