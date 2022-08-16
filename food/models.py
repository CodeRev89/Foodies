from django.db import models


from django.db import models
from django.contrib.auth.models import User
# remove unused imports
# User model not used in the project, will be problematic when attempting to permissions and retrieving recipes created by a specific user

# class User(User):
    
# removed commented code 
class Recipe(models.Model):
   dish_name=models.CharField(max_length=50)
   calories=models.CharField(max_length= 50)
   ingredients=models.CharField(max_length=250) # because we have declared a relation in the ingredient with the recipe, this field is not needed, ingredients can 
  
       
class Category(models.Model):
   origin=models.CharField(max_length=50)
   items_used=models.CharField(max_length=500)
   recipes= models.ManyToManyField(Recipe, related_name="recipes") # related name needs to be changed to category, will cause confusion later
   
   
class Ingredients(models.Model):
    recipes=models.ManyToManyField(Recipe, related_name="Recipes") 
    categories=models.ManyToManyField(Category, related_name="catergory")
    origin=models.CharField(max_length=50)
    produce_type=models.CharField(max_length=50)
    name= models.CharField(max_length=500,default=00)
    # need to implement better related_names for the recipes and categories fields

