from django.http.response import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.parsers import JSONParser
from .models import User, Post, Comment, UpVote
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.views import APIView
from django.db.utils import IntegrityError


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserSignUpViewSet(APIView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        json_response = request.data
        if (
            "email" not in json_response
            or "username" not in json_response
            or "password" not in json_response
        ):
            return JsonResponse(
                {
                    "error": "Not enough data to create new user. \
Provide email, username and password fields"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        email = json_response["email"]
        username = json_response["username"]
        password = json_response["password"]
        try:
            new_user = User.objects.create_user(
                email=email, username=username, password=password
            )
        except IntegrityError:
            return JsonResponse(
                {"error": "Email is already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return JsonResponse({"user_public_id": new_user.public_id})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvotePost(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse(
                {"error": "The tutorial does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return post

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get("post_id")
        user_public_id = request.user.public_id
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse(
                {"error": "Post does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(public_id=user_public_id)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            upvote = UpVote(author=user, post=post)
            upvote.save()
        except IntegrityError:
            return JsonResponse(
                {"error": "User already upvoted current post"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return JsonResponse(
            {
                "upvote_id": upvote.id,
            },
            status=status.HTTP_200_OK,
        )
