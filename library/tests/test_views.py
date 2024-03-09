import pytest

from django.urls import reverse
from django.test import Client
from library.models import Book
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_book_info_view():
    # Create a test client, which behaves like a simplified browser
    client = Client()
    # Create a book using the Book model
    book = Book.objects.create(author = "Dominique Roques", title = "Pico Bogue")
    # Request the retrieved URL
    path = reverse("info", args=[str(book.id)])
    response = client.get(path)
    # Decode the HTML response
    content = response.content.decode()

    # TBC
