from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



from .models import Post
from .forms import PostForm
from .decorators import check_draft


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


@login_required(login_url='/login/')
@check_draft
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, "post/post_detail.html", {"object": post})


class PostFruitMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PostFruitMixin, self).get_context_data(**kwargs)
        context["has_post"] = True
        return context


class PostMixinListView(PostFruitMixin, TemplateView):
    template_name = "post/mixin.html"