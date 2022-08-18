from django import forms
from django.contrib.auth import get_user_model
from .models import Recipe, Ingredients, Catergory



User = get_user_model()


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }
        
        
class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    

    
class RecipeForm(forms.ModelForm):
    class Meta:
        model= Recipe
        fields= ["dish_name", "calories"]
        
class IngredientForm(forms.ModelForm):
    class Meta:
        model =Ingredients
        fields = ["recipes", "categories", "origin", "produce_type", "name"]
        
class Catergoryform(forms.ModelForm):
    class Meta:
     model= Catergory
     fields=["origin", "recipes"]