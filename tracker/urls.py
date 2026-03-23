from django.urls import path
from . import views

urlpatterns = [
    path('', views.history, name='history'),          # List/Display (Home)
    path('log/', views.add_log, name='add_log'), 
    path('menu/', views.meallist, name='meallist'),          # Create
    # Later you can add path('edit/<int:pk>/', ...) for Edit/Delete
]

