from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    public_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def set_password(self, password):
        self.password = make_password(password)


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvote_amount = models.IntegerField(default=0)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
