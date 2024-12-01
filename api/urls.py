from django.contrib import admin
from django.urls import path
from home.views import index,person

urlpatterns = [
    path('get_courses', index),
    path('person/', person),
]
