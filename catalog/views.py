from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author


# Create your views here.

class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        books = Book.objects.all()
        params = {
            'title': "All",
            'books': books

        }
        return render(request, self.template_name, params)

class BookView(TemplateView):
    template_name = "catalog/book.html"

    def get(self, request, id):
        book = Book.objects.get(id=id)

        params = {
            'title': f"{book.title} detail",
            'book': book
        }

        return render(request, self.template_name, params)





class AuthorsView(TemplateView):
    template_name = "catalog/authors.html"

    def get(self, request):
        authors = Author.objects.all()

        params = {
            'authors': authors

        }
        return render(request, self.template_name, params)

class AuthorCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, first_name, last_name, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)

        params = {
            'title': f"{last_name}'s",
            'author': author,
            'books': books
        }
        return render(request, self.template_name, params)

class SearchView(TemplateView):
    template_name = "catalog/catalog.html"

    def post(self, request):
        search = request.POST('search')
        books_by_title = Book.objects.filter(title__icontans=search)

        params = {
            'search': search
        }




