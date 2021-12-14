from django.contrib import admin
from django.urls import path,include
from herokuapp import views

urlpatterns = [
    path("", views.index, name='home'),
]