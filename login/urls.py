# -*- coding: utf-8 -*-
from django.urls import path
from . import views
app_name = 'login'


urlpatterns = [
    path('log_out/', views.log_out, name='log_out'),
    path('login_to/',views.login_to, name='login_to'),
    path('index/', views.index, name='index'),
]
