from django.urls import path, include
from . import views
from lmsmainapp.views import*
from User import views as api_views

urlpatterns = [
    path('', views.temp, name='index'),
    # path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('vexam/', views.vexam, name='vexam'),
    # path('tutorial/', views.tutorial, name='vclass'),
    path('404/', views.error404, name='404'),
    path('vcourse/<int:id>', views.vcourse, name='vcourse'),
    path('vclass/<int:id>', views.vclass, name='vclass'),

###################comment############################

]