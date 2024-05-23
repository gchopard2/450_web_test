import pytest

from django.test import Client, TestCase
from library.models import DVD

class DVDModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Création du DVD
        DVD.objects.create(title = "Pico Bogue", duration = 120, pegi = "16+", description = "Pico Bogue - a great movie")

    def test_dvd_model_str(self):
        # Obtenir le DVD de la BD
        dvd = DVD.objects.get(id=1)

        # Valeur attendue
        expected_value = "Pico Bogue | 120mn | 16+ | Pico Bogue - a great movie"
        
        # Tester
        assert str(dvd) == expected_value
    def test_dvd_model_content(self):
        # Obtenir le DVD de la BD
        dvd = DVD.objects.get(id=1)

        # Valeurs attendue
        title_field = "Pico Bogue"
        duration_field = 120
        pegi_field = "16+"
        description_field = "Pico Bogue - a great movie"

        # Tester
        assert title_field == dvd.title
        assert duration_field == dvd.duration
        assert pegi_field == dvd.pegi
        assert description_field == dvd.description