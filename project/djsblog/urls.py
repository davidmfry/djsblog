from django.conf.urls import patterns, include, url
#from django.contrib.auth.decorators import login_required
#from django.views.static import serve as ServeStaticFile

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib import messages
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from os import path
import settings

from django.conf.urls.defaults import patterns, include, url
from blogengine.views import PostsFeed
from django.views.generic import ListView
from blogengine.models import Category, Post

urlpatterns = patterns('',

    #
    # Uncomment the next line to enable the admin:
    #
    url( r'^admin/', include( admin.site.urls ) ),

    #
    # Home page
    #
    url(r'^(?P<page>\d+)?/?$', ListView.as_view( model=Post, paginate_by=5, ) ),

    #
    # Blog Posts Detail
    #
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),

    #
    # Categories
    #
    url(r'^categories/?$', ListView.as_view(
        model=Category,
        )),
    url(r'^categories/(?P<categorySlug>\w+)/?$', 'blogengine.views.getCategory'),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'blogengine.views.getCategory'),

    #
    # Comments
    #
    url(r'^comments/', include('django.contrib.comments.urls')),

    #
    # RSS feeds
    #
    url(r'^feeds/posts/$', PostsFeed()),

)

