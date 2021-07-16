from rest_framework import serializers
from .models import User, Post, Comment
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("public_id", "username", "email", "password")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.public_id = uuid4()
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "link", "creation_date", "author")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "content", "creation_date", "author", "post")
