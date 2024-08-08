from django.shortcuts import render, redirect
from django.urls import path, include
from . import views
from django.contrib import admin
from django.http import HttpResponse
from .models import Recipe  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        carbohydrates = request.POST.get('carbohydrates')
        fats = request.POST.get('fats')
        proteins = request.POST.get('proteins')
        
        # Convert to integers if they are not empty
        carbohydrates = int(carbohydrates) if carbohydrates else None
        fats = int(fats) if fats else None
        proteins = int(proteins) if proteins else None
        
        if title and ingredients and instructions:
            Recipe.objects.create(
                title=title,
                ingredients=ingredients,
                instructions=instructions,
                carbohydrates=carbohydrates,
                fats=fats,
                proteins=proteins
            )
            return HttpResponse("Recipe submitted successfully!")
        else:
            return HttpResponse("Please fill in the title, ingredients, and instructions.")
    else:
        return render(request, 'add_recipe.html')
@login_required
def recipes(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'recipes': all_recipes})
@login_required
def about(request):
    return render(request, 'about.html')

