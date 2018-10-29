from django.urls import path
from restapi import views
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import *

urlpatterns = [
    url(r'^$',
        views.home,
        name='directory_home',),

    # http://localhost:8000/restapi/api/v1/marvel_heroes/1837
    url(r'^api/v1/(?P<document_type>[a-z0-9_]*)/$',
        csrf_exempt(views.api_documents),
        name='api'),

    # http://localhost:8000/restapi/api/v1/marvel_heroes
    url(r'^api/v1/(?P<document_type>[a-z0-9_]*)/(?P<document_id>\d+)/$',
        csrf_exempt(views.api_document_type),
        name='api'),


    # api/v1/{document_type}(i.e. heroes villans stats)/{document_type_id}(i.e the unqiue identifier)
    # preset document types: marvel_villans, marvel_heroes, marvel_stats
]
