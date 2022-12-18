from django.contrib import admin

from .models import NewsStory, Category 

# Register your models here.

admin.site.register(NewsStory) 
admin.site.register(Category)