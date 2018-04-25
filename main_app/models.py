from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.name)

class Subcategory(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.name)

class Recipe(models.Model):
    id_category = models.ForeignKey(
        'Category',
        on_delete = models.CASCADE,
    )
    id_subcategory = models.ForeignKey(
        'Subcategory',
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length = 50)
    difficulty = models.IntegerField(
        default = 1,
        validators = [MaxValueValidator(5), MinValueValidator(1)],
        )
    #minuti
    preparation_time_min = models.IntegerField(
        default = 1,
        validators = [MaxValueValidator(400), MinValueValidator(1)],
        )
    preparation = models.CharField(max_length = 5000)
    image = models.ImageField(upload_to='recipe_images',
                              default='media/default.jpg')
    def __str__(self):
        return str(self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.name)

class IngredientRecipe(models.Model):
    class Meta:
        unique_together = (('id_recipe','id_ingredient'),)
    id_recipe = models.ForeignKey(
        'Recipe',
        on_delete = models.CASCADE,
    )
    id_ingredient = models.ForeignKey(
        'Ingredient',
        on_delete = models.CASCADE,
    )
    amount = models.CharField(max_length = 20)
    def __str__(self):
        return '%s %s %s' %(self.id_recipe, self.id_ingredient, str(self.amount))
