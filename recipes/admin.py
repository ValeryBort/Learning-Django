from django.contrib import admin

from .models import Ingredient, IngredientList

admin.site.register(Ingredient)
admin.site.register(IngredientList)
