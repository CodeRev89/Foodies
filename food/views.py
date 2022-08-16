from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegister, UserLogin, Recipe
from django.contrib.auth import login, authenticate, logout
from .models import User


def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("successful-signup")
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
                return redirect("successful-login")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("success-page")


def create_view(request):
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


def create_view(request):
    form = ingredients()
    if request.method == "POST":
        form = ingredients(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context ={"form": form,}
    return render (request, "create_page.html", context)

def create_view(request):
    form= category()
    if request.method=="POST":
        form = category(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context={"form": form,}
    return render (request, "create_page.html", context)
# Create your views here.
