import pytest

from django.test import Client, TestCase
from library.models import Book

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(author = "Dominique Roques", title = "Pico Bogue")

    def test_book_model_str(self):
        book = Book.objects.get(id=1)
        expected_value = "Dominique Roques | Pico Bogue"
        
        assert str(book) == expected_value

    def test_book_model_content(self):
        book = Book.objects.get(id=1)
        author_field = book.author
        title_field = book.title
        
        assert author_field == "Dominique Roques"
        assert title_field == "Pico Bogue"
