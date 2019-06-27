# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 01:31:15 2019

@author: JM
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='social_login'),
    path('social/', include('social_django.urls',namespace='social')),
]
