from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    #url(r'^admin/', include(admin.site.urls)),
)
