from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from smartMove import views

urlpatterns = patterns('',
    url(r'^showHouses/$', views.showHouses, name='List of Houses'),
    url(r'^index/$', views.index, name='index'),
)
