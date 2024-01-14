from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path("", views.index, name='Home'),
    path("Authors", views.Authors, name='Authors'),
    path("About", views.About, name='About' ),
]
