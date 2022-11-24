from django.urls import path, include
from . import views
from lmsmainapp.views import*


urlpatterns = [
    path('', views.temp, name='index'),
    path('vexam/', views.vexam, name='vexam'),
]