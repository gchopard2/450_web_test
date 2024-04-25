import pytest

from django.test import Client, TestCase
from library.models import Book

AmountToCreate = 10

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(AmountToCreate):
            Book.objects.create(author = "Dominique Roques "+str(i), title = "Pico Bogue "+str(i))

    def test_book_model_str(self):
        for i in range(AmountToCreate):
            book = Book.objects.get(id=i+1)
            expected_value = "Dominique Roques "+str(i)+" | Pico Bogue "+str(i)
            
            assert str(book) == expected_value

    def test_book_model_content(self):
        for i in range(AmountToCreate):
            book = Book.objects.get(id=i+1)
            author_field = book.author
            title_field = book.title
            
            assert author_field == "Dominique Roques "+str(i)
            assert title_field == "Pico Bogue "+str(i)
    def test_book_count(self):
        assert Book.objects.count() == AmountToCreate
