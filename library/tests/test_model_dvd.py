import pytest

from django.test import Client, TestCase
from library.models import DVD

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        DVD.objects.create(title = "Pico Bogue", duration = 120, pegi = 18, description = "Pico Bogue - a great movie")

    def test_book_model_str(self):
        dvd = DVD.objects.get(id=1)
        expected_value = "Pico Bogue | 120mn | 18 | Pico Bogue - a great movie"
        
        assert str(dvd) == expected_value
