from django.shortcuts import render, redirect
from .models import Meal, Review # Import your models
from django.contrib.auth.decorators import login_required

@login_required # Security: Only logged-in users can log meals
def add_meal_view(request):
    """
    Handles the Create functionality for MJ Takeaway logs.
    """
    if request.method == "POST":
        # 1. Get data from the HTML form (Requirement #3: Create)
        restaurant_name = request.POST.get('restaurant')
        meal_name = request.POST.get('meal_name')
        tolerance = request.POST.get('tolerance')
        notes = request.POST.get('notes')

        # 2. Save to the Relational Database (Requirement #1 & #2)
        # Note: In a real app, you'd link this to a specific Restaurant object
        new_review = Review.objects.create(
            user=request.user,
            meal_name=meal_name, # Simplified for this example
            restaurant_name=restaurant_name,
            tolerance_rating=tolerance,
            notes=notes
        )
        
        # 3. Redirect to the list of all meals (Requirement #3: Locate/Display)
        return redirect('meal_list')

    # If it's a GET request, just show the empty form
    return render(request, 'add_meal.html')