import random
from django.shortcuts import render
from .models import Recipe
def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'main': recipes})
def category_detail(request):
    recipes = Recipe.objects.get(name="Category")
    return render(request, 'category_detail.html', {'category_detail': recipes})
def category_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'category_list.html', {'category_list': recipes})
def recipe_list(request):
    recipes = Recipe.objects.get()
    return render(request, 'recipe_detail.html', {'recipe_detail': recipes})