from django import forms
from .models import Post, Comment, Image

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("auther", "title", "text", "publish", "limited_publish",)


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ("src",)
        extra=5

class CommentUpdateForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('approved_comment',)





# ImageFormset = forms.inlineformset_factory(
#     Possrct,Image, fields= (('__all__')),
#     extra=5,
