from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path ('main/',name="main"),
    path('recipe_list/',recipe_list,name="recipe_list"),
    path('category_detail/',category_detail,name="category_detail"),
    path('category_list/',category_list,name="category_list"),
]