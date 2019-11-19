from django.contrib.auth.models import User
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class IngredientList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f'{self.user}: {self.name}'
