"""Foodies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food.views import user_register, user_login, user_homepage, logout_view, recipe_create_view,catergory_create_view, ingredients_create_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_register, name="register_page"),
    path("login/", user_login, name="login_page"),
    path("homepage/", user_homepage, name="home_page"),
    path("logout/", logout_view, name="logout_page"),
    path("createrecipe/", recipe_create_view, name="create_recipe"),
    path("createcatergory/",catergory_create_view, name= "create_catergory"),
    path ("createingrediants/", ingredients_create_view, name="create_ingrediants")
    
    
]
