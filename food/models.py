from django.db import models



    
    
class Recipe(models.Model):
   dish_name=models.CharField(max_length=50)
   calories=models.CharField(max_length= 50)
   
  
       
class Catergory(models.Model):
   origin=models.CharField(max_length=50)
   recipes= models.ManyToManyField(Recipe, related_name="category")
   
   
class Ingredients(models.Model):
    recipes=models.ManyToManyField(Recipe, related_name="Recipes")
    categories=models.ManyToManyField(Catergory, related_name="catergory")
    origin=models.CharField(max_length=50)
    produce_type=models.CharField(max_length=50)
    name= models.CharField(max_length=500,default=00)