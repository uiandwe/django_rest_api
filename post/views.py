from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostResultsView(PostDetailView):
    template_name = "posts/results.html"


class PostUpdateView(UpdateView):
    model = Post

    def get_success_url(self):
        return reverse("posts:detail", kwargs={"pk": self.object.pk})