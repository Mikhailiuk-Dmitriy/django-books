from django.urls import path

from app import views

urlpatterns = [
    path("", views.ShowBooksView.as_view(), name="index"),
    path("authors", views.ShowAuthorView.as_view(), name="authors"),
    path("authors_list", views.AuthorListView.as_view(), name="authors_list"),
    path(
        "create_author", views.CreateAuthorView.as_view(), name="create_author"
    ),
    path("create_book", views.CreateBookView.as_view(), name="create_book"),
    path(
        "detail_book/<int:pk>",
        views.DetailBookView.as_view(),
        name="detail_book",
    ),
    path(
        "delete_author/<int:pk>",
        views.DeleteAutherView.as_view(),
        name="delete_author",
    ),
    path(
        "delete_book/<int:pk>",
        views.DeleteBookView.as_view(),
        name="delete_book",
    ),
    path(
        "show_authors_books/<int:pk>",
        views.show_authors_books,
        name="show_authors_books",
    ),
    path(
        "update_author/<int:pk>",
        views.UpdateAuthorView.as_view(),
        name="update_author",
    ),
    path(
        "update_book/<int:pk>",
        views.UpdateBookView.as_view(),
        name="update_book",
    ),
]
