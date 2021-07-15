from django.http.response import JsonResponse
from rest_framework import viewsets, permissions, status
from .models import User, Post, Comment, UpVote
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.views import APIView
from django.db.utils import IntegrityError


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, ) 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvotePost(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse(
                {'error': 'The tutorial does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return post

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        user_public_id = request.user.public_id
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse(
                {'error': 'Post does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(public_id=user_public_id)
        except User.DoesNotExist:
            return JsonResponse(
                {'error': 'User does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            upvote = UpVote(author=user, post=post)
        # post.is_valid()
            upvote.save()
        except IntegrityError:
            return JsonResponse(
                {'error': 'User already upvoted current post'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return JsonResponse({
            "upvote_id":  upvote.id,
            }, status=status.HTTP_200_OK)


class Login(APIView):
    permission_classes = (permissions.AllowAny, )

    def get_object(self, email):
        try:
            user = User.objects.get(email=email)
        except Post.DoesNotExist:
            return {'error': 'Invalid credentials'}
        return user

    def get(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        return JsonResponse({email: password})
