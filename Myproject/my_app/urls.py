"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from my_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),  
    path('login/',views.login,name='login'),
    path('main/',views.main,name='main'),
    path('index/',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('add_visitor/',views.add_visitor,name='add_visitor'),
    path('add_notice/',views.add_notice,name='add_notice'),
    path('add_event/',views.add_event,name='add_event'),
    path('member/',views.member,name='member'),
    path('maintenance/',views.maintenance,name='maintenance'),
    path('add_complaint/',views.add_complaint,name='add_complaint'),
    path('add_suggestion/',views.add_suggestion,name='add_suggestion'),
    path('photos/',views.photos,name='photos'),
    path('alluser/',views.alluser,name='alluser'),
    path('videos/',views.videos,name='videos'),
    path('notice/',views.notice,name='notice'),
    path('event/',views.event,name='event'),
    path('allvisitor/',views.allvisitor,name='allvisitor'),
    path('allcomplaint/',views.allcomplaint,name='allcomplaint'),
    path('allsuggestion/',views.allsuggestion,name='allsuggestion'),
    path('pdf',views.getpdf,name='pdf'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('newpassword',views.newpassword,name='newpassword'),
]
