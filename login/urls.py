# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:31:15 2019

@author: JM
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='social_login'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
