from django.db import models
from django.contrib.auth.models import User

class ChipShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Meal(models.Model):
    shop = models.ForeignKey(ChipShop, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100) # e.g., "Grilled Cod"
    is_fried = models.BooleanField(default=True)

class Dish(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MJLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    grease_level = models.IntegerField() # 1 (Dry) to 5 (Dripping)
    stomach_feeling = models.TextField() # #3 CRUD - Display
    created_at = models.DateTimeField(auto_now_add=True)