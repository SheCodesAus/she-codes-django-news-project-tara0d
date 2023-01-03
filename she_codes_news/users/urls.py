from django.urls import path 
from .views import CreateAccountView
from .views import UserProfileView
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name = "profile"),
    # path('fav/<int:pk>/', views.favourite_add, name='favourite_add'),
]