from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import NewsStory, Category
from .forms import StoryForm
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'all_stories'

    def get_queryset(self):
        '''Return all news stories.'''
        cat_id = self.request.GET.get("cat")
        if cat_id:
            return NewsStory.objects.filter(category=cat_id)
        else:
            return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['categories'] = Category.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(generic.UpdateView):
    model = NewsStory
    template_name = "news/updatePost.html"
    fields = ['title', 'pub_date', 'category', 'content', 'image']
    success_url = reverse_lazy('news:index')

class DeletePostView(generic.DeleteView):
    model = NewsStory
    template_name = "news/delete_post.html"
    success_url = reverse_lazy('news:index')
    context_object_name = "story"

# @ login_required
# def favourite_add(request, pk):
#     story = get_object_or_404(NewsStory, pk=pk)
#     user = request.id
#     if story.favourites.filter(id=user.id).exists():
#         story.favourites.remove(user)
#     else:
#         story.favourites.add(user)
#     return redirect('news:story', pk=story.id)


# def favourite_add(request, pk):
#     user = request.user.id
#     if story.favourites.filter(id=user.id).exists():
#         story.favourites.remove(user)
#     else:
#         story.favourites.add(user)
#     return redirect('news:story', pk=story.id)




