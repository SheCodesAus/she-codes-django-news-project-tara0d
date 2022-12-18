from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.db import models

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class NewsStory(models.Model):
    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "News Stories"

    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name = "stories" 
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="stories",blank=True,null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(max_length=200) 
    favourited_by = models.ManyToManyField(User, related_name="favourites", blank=True)



#     favourited_by = models.ManyToManyField(User, related_name="favourites", default=None, blank=True, null=True)



