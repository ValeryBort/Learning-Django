from django.urls import path

from recipes.views import ingredients_page

urlpatterns = [
    path('ingredient_lists/', ingredients_page),
]
