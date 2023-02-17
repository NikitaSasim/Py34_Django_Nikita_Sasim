from rest_framework import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['user', 'display_products', 'get_total_quantity', 'get_total_price']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.last_name')
    class Meta:
        model = Book
        fields = ['title', 'summary', 'publication_date', 'price', 'amount', 'genre', 'author', 'cover', 'get_genre']




class AuthorSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'photo']

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name',]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
