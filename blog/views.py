from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostCreateForm
from django.contrib import messages
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    ordering =['-created_at']
    paginate_by = 10
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    fields = ("title", "text", "publish", "limited_publish",)
    success_url = reverse_lazy('post_detail')
    template_name = "post_create.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    fields = ("title", "text", "publish", "limited_publish",)
    success_url = reverse_lazy('post_detail')
    template_name = "post_update.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = "post_delete.html"
