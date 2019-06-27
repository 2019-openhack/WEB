# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:31:15 2019

@author: JM, jisu
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.file_upload),
    path('sendRequest/', views.sendRequest),
]
