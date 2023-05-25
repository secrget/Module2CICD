from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeTestCase(TestCase):
    def setUp(self):
        self.recipe1 = Recipe.objects.create(title='Recipe 1', description='Description 1', ingredients='Ingredients 1', instructions='Instructions 1')
        self.recipe2 = Recipe.objects.create(title='Recipe 2', description='Description 2', ingredients='Ingredients 2', instructions='Instructions 2')

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertQuerysetEqual(response.context['main'], Recipe.objects.all(), transform=lambda x: x)

    def test_category_detail_view(self):
        response = self.client.get(reverse('category_detail', args=['Recipe 1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertEqual(response.context['recipes'], self.recipe1)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        self.assertQuerysetEqual(response.context['recipes'], Recipe.objects.all(), transform=lambda x: x)

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        self.assertQuerysetEqual(response.context['recipe'], Recipe.objects.all(), transform=lambda x: x)
# Create your tests here.
