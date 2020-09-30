from django.db import models
from django.conf import settings



class Post(models.Model):
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # publish = models.IntegerField
    publish = models.BooleanField(default=True)
    limited_publish = models.BooleanField(default=False)
    src = models.ImageField('添付画像', upload_to='media', blank=True, null=True)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments', null=True,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



# class Image(models.Model):
#     src = models.ImageField('添付画像', upload_to='media', blank=True)
#     target = models.ForeignKey(
#         Post, verbose_name='image',
#         blank=True, null=True,
#         on_delete=models.CASCADE
#     )