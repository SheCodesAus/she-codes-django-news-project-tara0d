from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.http import HttpResponseRedirect    #Are we allowed to import this?
from django.contrib.auth.decorators import login_required


from .models import CustomUser
from .forms import CustomUserCreationForm

from news.models import NewsStory

# Create your views here.

# @ login_required
# def favourite_list(request):
#     new = NewsStory.filter(favourites=request.user)
#     return = 

@ login_required
def favourite_add(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)
    if story.favourites.filter(id=request.user.id).exists():
        story.favourites.remove(request.user)
    else:
        story.favourites.add(request.user)
    return redirect('news:story', pk=story.id)
    # return redirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect(request.)

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView):
    model = CustomUser
    slug_field = "username"
    template_name = "users/userProfile.html"
    context_object_name = "author"

    # def get_queryset(self):
    #     """Filters favourited stories"""
    #     favourite_posts = NewsStory.objects.filter('favourited_by')
    #     return favourite_posts


# class UserListView(generic.ListView):     #If want to create a separate page with list of all users
#     model = CustomUser

