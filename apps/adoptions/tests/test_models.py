import pytest
from django.utils import timezone

from apps.adopters.models import Adopter
from apps.adoptions.models import Adoption
from apps.pets.models import Pet
from apps.shelters.models import Shelter


@pytest.mark.django_db
def test_create_adoption():
    shelter = Shelter.objects.create(
        name="ONG Teste",
        city="São Paulo",
        capacity=50,
    )

    pet = Pet.objects.create(
        name="Amora",
        species="dog",
        age=1,
        shelter=shelter,
    )

    adopter = Adopter.objects.create(
        full_name="Jadson Silva",
        email="jadson@email.com",
    )

    adoption = Adoption.objects.create(
        pet=pet,
        adopter=adopter,
        shelter=shelter,
        status="PENDING",
        adoption_date=timezone.now(),
    )

    assert adoption.id is not None  # type: ignore
    assert adoption.status == "PENDING"
    assert adoption.pet.name == "Amora"


@pytest.mark.django_db
def test_pet_cannot_be_adopter_twice():
    shelter = Shelter.objects.create(
        name="Abrigo Central",
        city="São Paulo",
        state="SP",
        email="contato@abrigo.com",
        phone="11999999",
        capacity=50,
    )

    pet = Pet.objects.create(
        name="Amora",
        species="Dog",
        age=1,
        shelter=shelter,
        status="available",
    )

    adopter = Adopter.objects.create(
        full_name="Jadson Silva",
        email="jadson@email.com",
        phone="11988888888",
    )

    Adoption.objects.create(
        pet=pet,
        adopter=adopter,
        shelter=shelter,
        adoption_date=timezone.now(),
    )

    with pytest.raises(Exception):
        Adoption.objects.create(
            pet=pet,
            adopter=adopter,
            shelter=shelter,
            adopted_at=timezone.now(),
        )
