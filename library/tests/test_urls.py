import pytest

from django.urls import reverse, resolve
from library.models import Book

@pytest.mark.django_db
def test_book_info_url():
    # Create a book using the Book model + DB save
    Book.objects.create(author = "Dominique Roques", title = "Pico Bogue")
    book = Book.objects.get(id=1)
    path = reverse("info", args=[str(book.id)])

    # Check if the URL is correct
    assert path == "/1"
    assert resolve(path).view_name == "info"
