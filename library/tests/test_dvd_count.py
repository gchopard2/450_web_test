import pytest

from django.test import Client, TestCase
from library.models import DVD

AmountToCreate = 10

class DVDModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(AmountToCreate):
            DVD.objects.create(title="Pico Bogue "+str(i), duration=120, pegi="16+", description="Pico Bogue - a great movie "+str(i))

    def test_dvd_model_str(self):
        for i in range(AmountToCreate):
            dvd = DVD.objects.get(id=i+1)
            expected_value = "Pico Bogue "+str(i)+" | 120mn | 16+ | Pico Bogue - a great movie "+str(i)
            
            assert str(dvd) == expected_value

    def test_dvd_model_content(self):
        for i in range(AmountToCreate):
            dvd = DVD.objects.get(id=i+1)
            title_field = dvd.title
            duration_field = dvd.duration
            pegi_field = dvd.pegi
            description_field = dvd.description
            
            assert title_field == "Pico Bogue "+str(i)
            assert duration_field == 120
            assert pegi_field == "16+"
            assert description_field == "Pico Bogue - a great movie "+str(i)

    def test_dvd_count(self):
        assert DVD.objects.count() == AmountToCreate

