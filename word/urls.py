# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:31:15 2019

@author: JM
"""

from django.urls import path
from . import views

urlpatterns = [
    path('word/', views.word_show, name='word_show'),
    path('mean/', views.word_mean, name='word_mean')
]
