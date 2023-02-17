from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre
from cart.models import Cart


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = serializers.CartSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





