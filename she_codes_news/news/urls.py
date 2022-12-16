from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('edit-story/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete-story/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
]
