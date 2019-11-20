from django.shortcuts import render

from recipes.models import IngredientList


def ingredients_page(request):
    ingredient_lists = IngredientList.objects.all()
    return render(request, 'recipes/ingredient_lists.html', {'ingredient_lists': ingredient_lists})
