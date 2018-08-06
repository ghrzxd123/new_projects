# -*- coding: utf-8 -*-
from django.urls import path
from . import views
app_name = 'user'


urlpatterns = [
    path('home/', views.UserView.as_view(),name='home'),
    path('', views.UserView.as_view()),
]
