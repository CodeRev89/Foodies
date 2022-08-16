from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegister, UserLogin, Recipe
from django.contrib.auth import login, authenticate, logout
from .models import User

# Remove unused/ repeated imports statements


def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("successful-signup") # Be sure that when testing this route, the associated url pattern and view for "successful-signup" actually exists
            # Secondly, based on the daily standup discussion, successful login/registration should redirect the user to the main page, where the list of recipes/categories will be displayed
            # So remember your objective when redirecting users
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
                return redirect("successful-login") # Reference the same comments for registration, lines 21-23

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("success-page") # Based on our conversation and my understanding of your project, this should really redirect the user to the login/registration page


def create_view(request): # should apply a better naming convention, this function name has been used three times, should be more descriptive, e.g. recipe_create_view
    form = Recipe()
    if request.method == "POST":
        form = Recipe(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context = {
        "form": form,
    }
    return render(request, 'create_page.html', context)
# One issue that will be apparent later in the updates, there is no automatic association between the user and the Recipes they create

def create_view(request): # same comment as line 55
    form = ingredients() # This is not imported and should start with a capital letter
    if request.method == "POST":
        form = ingredients(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context ={"form": form,}
    return render (request, "create_page.html", context)

def create_view(request): # same comment as line 55
    form= category() # This is not imported and should start with a capital letter
    if request.method=="POST":
        form = category(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context={"form": form,}
    return render (request, "create_page.html", context)
# Create your views here.
