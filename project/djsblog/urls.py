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

#
#
#  we use this for local development only 
#  to serve static files
#
#
def static(request, template_name):

    if not 'html' in template_name:
        template_name += '.html'

    return render_to_response( template_name, { 
        'page_name': "Static Page",
        'site': Site.objects.get_current(),
        'user': request.user
    })



urlpatterns = patterns('',

    #
    #  this block of URLS only covers serving local static media
    #
    url( r'^css/(?P<path>.*)$',  'django.views.static.serve', { 'document_root': '%s/css' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '%s/font'% path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^img/(?P<path>.*)$',  'django.views.static.serve', { 'document_root': '%s/img' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^image/(?P<path>.*)$',  'django.views.static.serve', { 'document_root': '%s/img' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),
    url( r'^js/(?P<path>.*)$',   'django.views.static.serve', { 'document_root': '%s/js' % path.join( settings.ABSOLUTE_PATH, 'static').replace('\\','/') } ),


    #
    # Uncomment the next line to enable the admin:
    #
    url( r'^admin/', include( admin.site.urls ) ),

    #
    # Home page
    #
    url(r'^(?P<page>\d+)?/?$', ListView.as_view( model=Post, paginate_by=5, ) ),

    #
    # About page
    #
    url(r'^about/?$', 'blogengine.views.about' ),

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

