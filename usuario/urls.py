from django.urls import path
import usuario.views as views

urlpatterns = [
    path('', views.home_login),
    path('register/', views.register),
]