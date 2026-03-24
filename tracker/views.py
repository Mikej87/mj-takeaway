from django.views.generic import ListView  
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import MJLog, Meal, Dish

@login_required
def add_log(request):
    if request.method == "POST":
        # Get the 'dish' ID from the form select name="dish"
        dish_id = request.POST.get('dish') 
        
        MJLog.objects.create(
            user=request.user,
            dish_id=dish_id,  # Ensure this field name matches your MJLog model
            grease_level=request.POST.get('grease'),
            stomach_feeling=request.POST.get('feeling')
        )
        return redirect('history')
    
    # This part runs for the GET request (to show the form)
    dishes = Dish.objects.all() 
    return render(request, 'add_log.html', {'dishes': dishes})


@login_required
def history(request):
    logs = MJLog.objects.filter(user=request.user)
    return render(request, 'history.html', {'logs': logs})


class MealListView(ListView):
    model = Meal
    template_name = 'meallist.html'  # This links it to your file!
    context_object_name = 'dishes'         