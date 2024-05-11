from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_qr'),
    path('create/', views.create, name='create_qr'),
]
