import pytest

from django.test import Client, TestCase
from library.models import DVD

class DVDModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        DVD.objects.create(title = "Pico Bogue", duration = 120, pegi = "16+", description = "Pico Bogue - a great movie")

    def test_dvd_model_str(self):
        dvd = DVD.objects.get(id=1)
        expected_value = "Pico Bogue | 120mn | 16+ | Pico Bogue - a great movie"
        
        assert str(dvd) == expected_value
    def test_dvd_model_content(self):
        dvd = DVD.objects.get(id=1)

        title_field = dvd.title
        duration_field = dvd.duration
        pegi_field = dvd.pegi
        description_field = dvd.description

        assert title_field == "Pico Bogue"
        assert duration_field == 120
        assert pegi_field == "16+"
        assert description_field == "Pico Bogue - a great movie"