from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostResultsView(PostDetailView):
    template_name = "post/results.html"


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse("posts:detail", kwargs={"pk": self.object.pk})