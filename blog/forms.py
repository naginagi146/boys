from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("auther", "title", "text", "publish", "limited_publish",)


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)