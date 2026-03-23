from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_list_view, name='meal_list'),
    path('add-meal/', views.add_meal_view, name='add_meal'),
]