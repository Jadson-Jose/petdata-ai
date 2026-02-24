import pytest
from apps.pets.models import Pet
from apps.shelters.models import Shelter


@pytest.mark.django_db
def test_create_pet():
    shelter = Shelter.objects.create(
        name="Abrigo Esperança",
        city="Campinas",
        state="SP",
        email="contato@abrigo.com",
        phone="19999999999",
        capacity=100,
    )

    pet = Pet.objects.create(
        name="Paçoca",
        species=Pet.Species.DOG,
        age=7,
        size=Pet.Size.MEDIUM,
        gender=Pet.Gender.MALE,
        shelter=shelter,
    )
