import random
from django.shortcuts import render, get_object_or_404
from .models import Recipe
def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'main': recipes})
def category_detail(request, title):
    recipes = get_object_or_404(Recipe, title=title)
    return render(request, 'category_detail.html', {'recipes': recipes})
def category_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'category_list.html', {'recipes': recipes})
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_detail.html', {'recipe': recipes})