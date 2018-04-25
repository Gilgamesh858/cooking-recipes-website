from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                          widget=forms.PasswordInput())

class addRecipeForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    category = forms.ModelChoiceField(queryset = Category.objects.all(), label='Category')
    subcategory = forms.ModelChoiceField(queryset = Subcategory.objects.all(), label='Subcategory')
    difficulty = forms.ChoiceField(label='Difficulty', choices=((str(x), x) for x in range(1,6)))
    preparation_time_min = forms.IntegerField(label='Preparation_time_min', max_value = 400, min_value = 1)

class addIngredientForm(forms.Form):
    ingredient = forms.CharField(label='Ingredient', max_length=30)
    amount = forms.CharField(label='Amount', max_length=20)
    misure = forms.ChoiceField(label ='Misure', choices=[("gr", "gr"),
                                                         ("kg", "Kg"),
                                                         ("lt", "lt"),
                                                         ("ml", "ml"),
                                                         ("pz", "pz"),
                                                         ("pizzico", "pizzico"),
                                                         ("cucchiaino/i", "cucchiaino/i"),
                                                         ("cucchiaio/ia", "cucchiaio/i"),
                                                         ("bicchiere/i", "bicchiere/i"),
                                                         ],)

class addRecipeFinalForm(forms.Form):
    preparation = forms.CharField(label='Preparation', max_length=5000,
                                  widget=forms.TextInput(attrs={'cols': 100, 'rows': 200}))
    image = forms.ImageField(label='Image', required=False)


class searchForForm(forms.Form):
    choice = forms.ChoiceField(label ='Choice', choices=[("name", "Titolo"),
                                                         ("category", "Categoria"),
                                                         ("subcategory", "Tipo di piatto"),
                                                         ("difficulty", "Difficolta'"),
                                                         ("preparation_time_min", "Tempo di preparazione")],
                                widget=forms.RadioSelect())

class searchFormName(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
class searchFormCat(forms.Form):
    category = forms.ModelChoiceField(queryset = Category.objects.all(), label='Category')
class searchFormSubC(forms.Form):
    subcategory = forms.ModelChoiceField(queryset = Subcategory.objects.all(), label='Subcategory')
class searchFormDif(forms.Form):
    difficulty = forms.ChoiceField(label='Difficulty', choices=((str(x), x) for x in range(1,6)))
class searchFormPrep(forms.Form):
    preparation_time_min = forms.IntegerField(label='Preparation_time_min', max_value = 400, min_value = 1)
