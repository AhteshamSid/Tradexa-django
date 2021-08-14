from django.db import models
from django.utils import timezone

from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'email']

    def __str__(self):
        return "{}".format(self.username)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    #
    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
