from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostCreateForm, CommentCreateForm
from django.contrib import messages
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering =['-created_at']
    paginate_by = 10
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')
    template_name = "blog/post_update.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)


    def form_invalid(self, form):
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = "blog/post_delete.html"

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.auther:
            return True
        return False

class PostDraftListView(ListView):
    model = Post
    context_object_name = 'drafts'
    paginate_by = 10
    template_name = "blog/post_draft.html"

    def get_queryset(self):
        return Post.objects.filter(publish=False)



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    success_url = reverse_lazy('post_list')
    template_name = "blog/comment_create.html"

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('blog/post_detail', pk=post_pk)




