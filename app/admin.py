from django.contrib import admin

from .models import Author
from .models import Book


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    pass
