from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import MJLog, Meal, Dish


def add_log(request):
    dishes = Dish.objects.all()  # Get all dishes from DB
    return render(request, 'add_log.html', {'dishes': dishes})


def meal_list(request):
    dishes = Dish.objects.all()  # Or whatever your model is called
    return render(request, 'meallist.html', {'dishes': dishes})


def add_log(request):
    if request.method == "POST":
        # Create logic
        meal_id = request.POST.get('meal')
        MJLog.objects.create(
            user=request.user,
            meal_id=meal_id,
            grease_level=request.POST.get('grease'),
            stomach_feeling=request.POST.get('feeling')
        )
        return redirect('history')
    
    meals = Meal.objects.all()
    return render(request, 'add_log.html', {'meals': meals})
@login_required
def history(request):
    # Display logic
    logs = MJLog.objects.filter(user=request.user)
    return render(request, 'history.html', {'logs': logs})