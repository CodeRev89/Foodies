from django.contrib import admin
from .models import Recipe, Catergory, Ingredients
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Catergory)
admin.site.register(Ingredients)