from os import sendfile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Image
from .forms import PostCreateForm, CommentCreateForm, ImageForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering =['-created_at']
    paginate_by = 10
    template_name = "blog/post_list.html"

    def get_queryset(self):
        queryset = Post.objects.all()
        if 'query' in self.request.GET:
            qs = self.request.GET['query']
            queryset =queryset.filter(name__contains=qs)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'image':Image.objects.all()})
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    form_class2 =ImageForm
    success_url = reverse_lazy('post_list')
    template_name = "blog/post_create.html"

    def get_context_data(self, **kwargs):
        context= CreateView.get_context_data(self, **kwargs)
        form2 = self.form_class2(self.request.GET)
        context.update({'form2':form2})
        return context


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



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "blog/comment_create.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail",kwargs={"pk":self.kwargs["pk"]} )



class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    ordering =['-created_at']
    paginate_by = 10
    template_name = "blog/comment_list.html"



# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('blog/post_detail', pk=comment.post.pk)


# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('blog/post_detail', pk=comment.post.pk)