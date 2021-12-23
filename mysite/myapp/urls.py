from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search)
    path('search/media', views.search.media)
]
