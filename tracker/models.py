from django.db import models
from django.contrib.auth.models import User


class ChipShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Meal(models.Model):
    shop = models.ForeignKey(ChipShop, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)  
    is_fried = models.BooleanField(default=True)


class Dish(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MJLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    grease_level = models.IntegerField() 
    stomach_feeling = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)