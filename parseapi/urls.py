from django.contrib import admin
from django.urls import path
from parseapi import views
urlpatterns = [
    path('',views.parseapi,name='parseapi'),

]
