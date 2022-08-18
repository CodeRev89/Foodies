from django.contrib.auth import login, authenticate, logout
from .forms import UserRegister, UserLogin, RecipeForm,Catergoryform, IngredientForm
from django.shortcuts import render, redirect
from .models import Catergory, Recipe, Ingredients



def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("home_page")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)



def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home_page")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def user_homepage(request):
    recipes= Recipe.objects.all()
    catergories = Catergory.objects.all()
    ingredients= Ingredients.objects.all()
    context = {"catergories":catergories,
               "recipes":recipes,
               "ingredients":ingredients,
    }
    print (context)
    return render(request, "homepage.html", context)

def logout_view(request):
    logout(request) 
    print("hello")
    return redirect("login_page")




def recipe_create_view(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {
        
        "form": form,
    }
    return render(request, 'create_recipe.html', context)


def ingredients_create_view(request):
    form = IngredientForm()
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context ={"form": form,}
    return render (request, "create_ingrediants.html", context)

def catergory_create_view(request):
    form= Catergoryform()
    if request.method=="POST":
        form = Catergoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context={"form": form,}
    return render (request, "create_catergory.html", context)
# Create your views here.
