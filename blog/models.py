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


    def __str__(self):
        return self.title
