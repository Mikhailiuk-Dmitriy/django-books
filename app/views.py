from typing import Any

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Author
from .models import Book


class ShowBooksView(generic.ListView):
    template_name = "app/index.html"
    model = Book
    context_object_name = "books"


class DetailBookView(generic.DetailView):
    template_name = "app/detail_book.html"
    model = Book


class DeleteBookView(generic.DeleteView):
    template_name = "app/delete_book.html"
    model = Book
    success_url = "/"


class UpdateBookView(generic.UpdateView):
    template_name = "app/update_book.html"
    model = Book
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        contex = super().get_context_data()
        contex["authors"] = Author.objects.all()
        return contex


class CreateBookView(generic.CreateView):
    template_name = "app/create_book.html"
    model = Book
    fields = "__all__"
    success_url = "/"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        contex = super().get_context_data()
        contex["authors"] = Author.objects.all()
        return contex


class ShowAuthorView(generic.ListView):
    template_name = "app/authors.html"
    model = Author
    context_object_name = "authors"


class CreateAuthorView(generic.CreateView):
    template_name = "app/create_author.html"
    model = Author
    fields = "__all__"
    success_url = "/authors"


class UpdateAuthorView(generic.UpdateView):
    template_name = "app/update_author.html"
    model = Author
    fields = "__all__"
    success_url = "/authors"


class DeleteAutherView(generic.DeleteView):
    template_name = "app/delete_author.html"
    model = Author
    success_url = "/authors"


class AuthorListView(generic.ListView):
    template_name = 'app/authors_list.html'
    model = Author
    context_object_name = "authors"


def show_authors_books(request, pk: int) -> HttpResponse:
    books = Book.objects.filter(author=pk)
    return render(request, 'app/show_authors_books.html', {'books': books})
