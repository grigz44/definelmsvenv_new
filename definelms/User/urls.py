from django.urls import path, include
from . import views
from lmsmainapp.views import*


urlpatterns = [
    path('', views.temp, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('vexam/', views.vexam, name='vexam'),
    path('vcourse/', views.vcourse, name='vcourse'),
]