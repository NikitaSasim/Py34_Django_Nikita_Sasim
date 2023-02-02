from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Genre


# Create your views here.

class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"


    def get(self, request):
        books = Book.objects.all()
        genres = Genre.objects.all()
        params = {
            'title': "All",
            'books': books,
            'genres': genres,

        }
        return render(request, self.template_name, params)


class BookView(TemplateView):
    template_name = "catalog/book.html"

    def get(self, request, id):
        book = Book.objects.get(id=id)
        genres = Genre.objects.all()

        params = {
            'title': f"{book.title} detail",
            'book': book,
            'genres': genres,
        }

        return render(request, self.template_name, params)


class AuthorsView(TemplateView):
    template_name = "catalog/authors.html"

    def get(self, request):
        authors = Author.objects.all()
        genres = Genre.objects.all()

        params = {
            'authors': authors,
            'genres': genres,

        }
        return render(request, self.template_name, params)


class AuthorCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, first_name, last_name, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)
        genres = Genre.objects.all()

        params = {
            'title': f"{last_name}'s",
            'author': author,
            'books': books,
            'genres': genres,
        }
        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = "catalog/catalog.html"

    def post(self, request):
        search = request.POST['search']
        books_by_title = Book.objects.filter(title__iregex=search)
        books_by_summary = Book.objects.filter(summary__iregex=search)
        books_by_publication_date = Book.objects.filter(publication_date__year__iregex=search)
        books_by_genre = Book.objects.filter(genre__name__iregex=search)
        books_by_last_name = Book.objects.filter(author__last_name__iregex=search)
        books_by_first_name = Book.objects.filter(author__first_name__iregex=search)
        books_by_price = Book.objects.filter(price__iregex=search)
        genres = Genre.objects.all()

        books_by_all = books_by_title.union(books_by_summary, books_by_publication_date, books_by_genre, books_by_last_name, books_by_first_name, books_by_price)

        params = {
            'books': books_by_all,
            'title': f"'{search}'",
            'genres': genres,
        }

        return render(request, self.template_name, params)


class GenreCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, id):
        genre = Genre.objects.get(id=id)
        books = Book.objects.filter(genre=genre)
        genres = Genre.objects.all()

        params = {
            'title': f"{genre.name}'s",
            'books': books,
            'genres': genres,
        }
        return render(request, self.template_name, params)
