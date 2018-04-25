from django.contrib import admin
from .models import Category
from .models import Subcategory
from .models import Recipe
from .models import Ingredient
from .models import IngredientRecipe

#Username -> admin
#Password -> passwordadmin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_category', 'id_subcategory', 'name', 'difficulty', 'preparation_time_min', 'preparation', 'image')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class IngredientRecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_recipe', 'id_ingredient', 'amount')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientRecipe, IngredientRecipeAdmin)
