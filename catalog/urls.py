from django.contrib import admin
from django.urls import path
from .views import CatalogView, AuthorsView, AuthorCatalogView, BookView, SearchView, GenreCatalogView


urlpatterns = [
    path("", CatalogView.as_view(), name="catalog-index"),
    path("catalog/book-<int:id>/", BookView.as_view(), name="catalog-book"),
    path("authors/", AuthorsView.as_view(), name="catalog-author"),
    path("authors/<str:first_name>-<str:last_name>-<int:id>/", AuthorCatalogView.as_view(), name="catalog-authors-author"),
    path("genres/genre-<int:id>", GenreCatalogView.as_view(), name="catalog-genres"),
    path("catalog/search/", SearchView.as_view(), name='catalog-search')
]
