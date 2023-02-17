from django.urls import path
from .views import UserList, BookList, AuthorList, GenreList, BookDetail, CartList

urlpatterns = [
    path("users/", UserList.as_view(), name="api-user"),
    path("books/", BookList.as_view(), name="api-book"),
    path("book-<int:pk>/", BookDetail.as_view(), name="api-book-detail"),
    path("authors/", AuthorList.as_view(), name="api-authors"),
    path("genres/", GenreList.as_view(), name="api-genre"),
    path("carts/", CartList.as_view(), name="api-cart")

]