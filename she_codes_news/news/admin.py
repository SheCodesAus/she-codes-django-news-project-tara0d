from django.contrib import admin

from .models import NewsStory, Category        #added

# Register your models here.

admin.site.register(NewsStory)      #added
admin.site.register(Category)



