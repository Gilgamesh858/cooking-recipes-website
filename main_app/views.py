from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
#Usato per il FormSet
from django.views.generic import CreateView

# Create your views here.
def index(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html')

def cookbook(request):
    book = Subcategory.objects.all()
    print(book)
    return render(request, 'cookbook.html')

def search(request):
    return render(request, 'search.html')

def contact(request):
    return render(request, 'contact.html')

def profile_view(request, user_name):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profile/'+u)
                else:
                    print("The account has been disabled!")
            else:
                print("The username and password were incorrect.")
                return render(request, 'login.html', {'flag': True, 'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html',
                              {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    flagUs = False
    flagEmail = False
    flagPassword = False

    #if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        if password1 != password2 :
            flagPassword = True
        else:
            try:
                username1 = User.objects.get(username=username)
                flagUs = True
            except User.DoesNotExist:
                flagUs = False

            try:
                email1 = User.objects.get(email=email)
                flagEmail = True
            except User.DoesNotExist:
                flagEmail = False

            if flagEmail == False and flagUs == False:
                user = User.objects.create_user(username=username,password=form.cleaned_data['password1'],email=email)
                return HttpResponseRedirect('/login')
    #form = RegistrationForm()
    return render(request, 'register.html', {'flagPassword': flagPassword, 'flagEmail': flagEmail, 'flagUs': flagUs, 'form': form})

def search_view(request, choice1):
    recipe_obj = None
    recipe = None
    form = None

    if choice1 == 'name' or choice1 == "name1":
        form = searchFormName(request.POST)

    if choice1 == 'category' or choice1 == 'category1':
        form = searchFormCat(request.POST)

    if choice1 == 'subcategory' or choice1 == 'subcategory1':
        form = searchFormSubC(request.POST)

    if choice1 == 'difficulty' or choice1 == 'difficulty1':
        form = searchFormDif(request.POST)

    if choice1 == 'preparation_time_min' or choice1 == 'preparation_time_min1':
        form = searchFormPrep(request.POST)

    if request.method == 'POST':
        choice = None

        if form.is_valid():
            if 'name1' in request.POST:
                # search recipe for name
                choice = form.cleaned_data['name']
                print(" ")
                print(choice)
                print(" ")
                try:
                    recipe_obj = Recipe.objects.filter(name__icontains=choice)
                    r2 = Recipe.objects.get(name="Fecola")
                except Recipe.DoesNotExist:
                    print("Errore. Ricette Inesistenti.")

            if 'category1' in request.POST:
                # search recipe for category
                choice = form.cleaned_data['category']
                print(" ")
                print(choice)
                print(" ")
                try:
                    recipe_obj = Recipe.objects.filter(id_category=choice)
                except Recipe.DoesNotExist:
                    print("Errore. Ricette Inesistenti.")

            if 'subcategory1' in request.POST:
                # search recipe for subcategory
                choice = form.cleaned_data['subcategory']
                try:
                    recipe_obj = Recipe.objects.filter(id_subcategory=choice)
                except Recipe.DoesNotExist:
                    print("Errore. Ricette Inesistenti.")

            if 'difficulty1' in request.POST:
                # search recipe for difficulty
                choice = form.cleaned_data['difficulty']
                try:
                    recipe_obj = Recipe.objects.filter(difficulty=choice)
                except Recipe.DoesNotExist:
                    print("Errore. Ricette Inesistenti.")

            if 'preparation_time_min1' in request.POST:
                # search recipe for preparation_time_min
                choice = form.cleaned_data['preparation_time_min']
                try:
                    recipe_obj = Recipe.objects.filter(preparation_time_min__lte=choice)
                except Recipe.DoesNotExist:
                    print("Errore. Ricette Inesistenti.")

            count = 0
            recipe = []

            for key in recipe_obj:
                recipe.append({count:" "})
                recipe_list = {"id":key.id, "name": key.name, "category":key.id_category, "subcategory":key.id_subcategory, "difficulty":key.difficulty, "preparation_time_min":key.preparation_time_min}
                print("recipe_list -> " + str(recipe_list))
                recipe[count] = recipe_list
                count = count + 1

            return render(request, 'searchFor.html', {'form':form, 'recipe': recipe, 'choice1': choice1})

    return render(request, 'searchFor.html', {'form':form, 'choice1': choice1})

def searchFor_view(request):
    form = searchForForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            choice = form.cleaned_data['choice']
            #return render(request, 'searchFor.html', {'choice': choice})
            return HttpResponseRedirect('%s/' % choice)

    return render(request, 'search.html', {"form": form})

def show_recipe(request, recipe_id):
    try:
        recipe_obj = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        print("Errore. Ricette Inesistenti.")

    try:

        ingredientRecipe_obj = IngredientRecipe.objects.filter(id_recipe = recipe_id)
        recipe = {
            "id": recipe_obj.id,
            "name": recipe_obj.name,
            "category": recipe_obj.id_category,
            "subcategory": recipe_obj.id_subcategory,
            "difficulty": recipe_obj.difficulty,
            "preparation_time_min": recipe_obj.preparation_time_min,
            "preparation": recipe_obj.preparation,
            "image":recipe_obj.image}
        ingredient_dict1 = []
        amount_dict1 = []

        for j in ingredientRecipe_obj:
            ingredient_dict1.append(str(j.id_ingredient))
            ingredient_dict1.append(j.amount)

            #recipe.update({"ingredient": j.id_ingredient, "amount": j.amount})
        recipe.update({"ingredient": ingredient_dict1})

    except IngredientRecipe.DoesNotExist:
        print("Errore. Ingredienti Inesistenti.")

    return render(request, 'showRecipe.html', {'context': recipe})

def cookbook(request):
    context = None
    try:
        latest_recipe = Recipe.objects.latest('id')
    except Recipe.DoesNotExist:
        print("Errore. Ricette Inesistenti.")
        return render(request, 'cookbook.html', {'context': context})

    latest_id = latest_recipe.id
    i = 0
    context = {}

    try:
        recipe_obj = Recipe.objects.all().order_by('-id')[:5][::1]
    except Recipe.DoesNotExist:
        print("Errore. Ricette Inesistenti.")

    try:
        for key in recipe_obj:
            ingredientRecipe_obj = IngredientRecipe.objects.filter(id_recipe = key.id)
            context.update({i:" "})

            recipe = {
                "id": key.id,
                "name": key.name,
                "category": key.id_category,
                "subcategory": key.id_subcategory,
                "difficulty": key.difficulty,
                "preparation_time_min": key.preparation_time_min,
                "preparation": key.preparation[:500]+"...",
                "image":key.image}
            ingredient_dict1 = []
            amount_dict1 = []

            for j in ingredientRecipe_obj:
                ingredient_dict1.append(str(j.id_ingredient))
                ingredient_dict1.append(j.amount)

                #recipe.update({"ingredient": j.id_ingredient, "amount": j.amount})
            recipe.update({"ingredient": ingredient_dict1})

            context[i] = recipe
            i = i + 1

    except IngredientRecipe.DoesNotExist:
        print("Errore. Ingredienti Inesistenti.")

    return render(request, 'cookbook.html', {'context': context})

'''
    for i in range(0,5):
        try:
            recipe_obj = Recipe.objects.get(id = latest_id)
            recipe_obj = Recipe.objects.filter(since=since).order_by('-id')[:10][::-1]

        except Recipe.DoesNotExist:
            break

        try:
            ingredientRecipe_obj = IngredientRecipe.objects.filter(id_recipe = recipe_obj.id)

        except IngredientRecipe.DoesNotExist:
            break

        recipe = {
             "id": recipe_obj.id,
             "name": recipe_obj.name,
             "category": recipe_obj.id_category,
             "subcategory": recipe_obj.id_subcategory,
             "difficulty": recipe_obj.difficulty,
             "preparation_time_min": recipe_obj.preparation_time_min,
             "preparation": recipe_obj.preparation,
             "image":recipe_obj.image}

        for j in ingredientRecipe_obj:
            recipe.update({"ingredient": j.id_ingredient, "amount": j.amount})

        context[i] = recipe
        latest_id = latest_id - 1
    return render(request, 'cookbook.html', {'context': context})
'''

def recipe_create_view(request):
    stepC1 = False
    stepC2 = False
    stepC3 = False

    if 'go' in request.POST:
        stepC1 = True
        stepC2 = False
        stepC3 = False

    if 'step1' in request.POST:
        stepC1 = False
        stepC2 = True
        stepC3 = False

    if 'step2' in request.POST:
        stepC1 = False
        stepC2 = False
        stepC3 = True

    form1 = addRecipeForm(request.POST)
    form2 = addIngredientForm(request.POST)
    form3 = addRecipeFinalForm(request.POST)

    if request.method == 'POST':
        if 'step1' in request.POST:
            stepC1 = False
            stepC2 = True
            stepC3 = False
            form1 = addRecipeForm(request.POST)

            if form1.is_valid():
                name = form1.cleaned_data['name']
                category = form1.cleaned_data['category']
                subcategory = form1.cleaned_data['subcategory']
                difficulty = form1.cleaned_data['difficulty']
                preparation_time_min = form1.cleaned_data['preparation_time_min']
                preparation = "blank"
                image = "default.jpg"

                try:
                    recipe_obj = Recipe.objects.get(name = name)
                    recipe_obj.save()

                except Recipe.DoesNotExist:
                    recipe_obj = Recipe(id_category = category, id_subcategory = subcategory, name = name, difficulty = difficulty, preparation_time_min = preparation_time_min, preparation = preparation, image = image)
                    recipe_obj.save()

            return render(request, 'addRecipe.html', {'recipe':recipe_obj.id, 'stepC1': stepC1, 'stepC2': stepC2, 'stepC3': stepC3, 'form1': form1, 'form2':form2})

        if 'step2' in request.POST or 'newIngredient' in request.POST:
            if 'newIngredient' in request.POST:
                stepC1 = False
                stepC2 = True
                stepC3 = False
            else:
                stepC1 = False
                stepC2 = False
                stepC3 = True

            form2 = addIngredientForm(request.POST)

            if form2.is_valid():
                ingredient = form2.cleaned_data['ingredient']
                amount = form2.cleaned_data['amount']
                misure = form2.cleaned_data['misure']
                amount = amount + " " + misure

                try:
                    ingredient_obj = Ingredient.objects.get(name=ingredient)

                except Ingredient.DoesNotExist:
                    ingredient_obj = Ingredient(name=ingredient)
                    ingredient_obj.save()

                name = request.POST['recipe_name_label']
                recipe_db = Recipe.objects.get(id=name)

                try:
                    ingr_recipe_obj = IngredientRecipe.objects.get(id_recipe = recipe_db, id_ingredient = ingredient_obj, amount =amount)
                    ingr_recipe_obj.save()

                except IngredientRecipe.DoesNotExist:
                    ingr_recipe_obj = IngredientRecipe(id_recipe = recipe_db, id_ingredient = ingredient_obj, amount =amount)
                    ingr_recipe_obj.save()

                try:
                    ingr_recipe_array = IngredientRecipe.objects.filter(id_recipe = recipe_db).order_by('-id_ingredient')

                except IngredientRecipe.DoesNotExist:
                    ingr_recipe_array = " "

            return render(request, 'addRecipe.html', {'ingredient_added': ingr_recipe_array, 'recipe': recipe_db.id, 'stepC1': stepC1, 'stepC2': stepC2, 'stepC3': stepC3, 'form1': form1, 'form2': form2, 'form3':form3})

        if 'step3' in request.POST:
            stepC1 = True
            stepC2 = False
            stepC3 = False
            form3 = addRecipeFinalForm(request.POST, request.FILES)

            if form3.is_valid():
                preparation = form3.cleaned_data['preparation']

                if len(request.FILES) != 0:
                    image = form3.cleaned_data['image']
                else:
                    image = "default.jpg"

                name = request.POST['recipe_name_label']
                recipe_db = Recipe.objects.get(id=name)

                recipe_db.preparation = preparation
                recipe_db.image = image
                recipe_db.save()

                return HttpResponseRedirect('/')

    return render(request, 'addRecipe.html', {'stepC1': stepC1, 'stepC2': stepC2, 'stepC3': stepC3, 'form1': form1, 'form2': form2, 'form3': form3})
