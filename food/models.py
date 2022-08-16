from django.db import models


from django.db import models
from django.contrib.auth.models import User

# class User(User):
    
    
class Recipe(models.Model):
   dish_name=models.CharField(max_length=50)
   calories=models.CharField(max_length= 50)
   ingredients=models.CharField(max_length=250)
  
       
class Category(models.Model):
   origin=models.CharField(max_length=50)
   items_used=models.CharField(max_length=500)
   recipes= models.ManyToManyField(Recipe, related_name="recipes")
   
   
class Ingredients(models.Model):
    recipes=models.ManyToManyField(Recipe, related_name="Recipes")
    categories=models.ManyToManyField(Category, related_name="catergory")
    origin=models.CharField(max_length=50)
    produce_type=models.CharField(max_length=50)