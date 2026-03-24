from django.contrib import admin
from .models import ChipShop, Meal, MJLog, Dish  

# This makes the ChipShop table editable in the admin panel
@admin.register(ChipShop)
class ChipShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)

# This makes the specific Meals editable
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'shop', 'is_fried')
    list_filter = ('is_fried', 'shop') # Handy filters on the right side

# This allows you to see what users are logging
@admin.register(MJLog)
class MJLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'meal', 'grease_level', 'created_at')
    readonly_fields = ('created_at',) # Prevents changing the date manually

    admin.site.register(Dish)