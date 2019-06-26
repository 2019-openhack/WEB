# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:31:15 2019

@author: JM
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_info, name='word_info'),
]