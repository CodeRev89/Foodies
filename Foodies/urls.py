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
from food.views import user_register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_register, name="register")
]


# Since there is a custom css file for styling
# 1) Configure the settings with the to have a STATIC_ROOT variable
# 2) Import settings here in the urls
# 3) Import the function static
# 4) Add conditional statement to check debug and append the static to the urlpatterns
# https://warehouse.joincoded.com/workshops/django-files/static-files/what-are-static-files
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development