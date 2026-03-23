from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=50) # e.g., Greek, Indian, Sushi

class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # e.g., "Chicken Shish Kebab"
    is_high_protein = models.BooleanField(default=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    # The "MJ Takeaway" specific data:
    tolerance_rating = models.IntegerField() # 1-5 (How did your stomach feel?)
    notes = models.TextField() # e.g., "Avoid the garlic sauce, too heavy!"
    created_at = models.DateTimeField(auto_auto_now_add=True)