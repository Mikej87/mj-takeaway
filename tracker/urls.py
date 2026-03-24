from django.urls import path
from . import views

urlpatterns = [
    path('', views.history, name='history'),          # List/Display (Home)
    path('log/', views.add_log, name='add_log'), 
    path('meals/', views.MealListView.as_view(), name='meal_list'),    
]

