from django.urls import path
from django.conf.urls import include #, url

from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    path('search', views.search),
    path('search/media/indianFlag.png', views.flag),
    path('search/media/favicon.ico', views.icon),
]
