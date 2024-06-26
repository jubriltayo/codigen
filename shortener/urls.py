from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<str:pk>/', views.shortened_url, name='shortened_url')   
]
