import pytest
from adopters.models import Adopter
from adoptions.models import Adoption
from django.utils import timezone
from pets.models import Pet
from shelters.models import Shelter


@pytest.mark.django_db
def test_create_adoption():
    shelter = Shelter.objects.create(
        name="ONG Teste",
        city="São Paulo",
    )

    pet = Pet.objects.create(
        name="Amora",
        species="dog",
        age=1,
        shelter=shelter,
    )

    adopter = Adopter.objects.create(
        name="Jadson Silva",
        email="jadson@email.com",
    )

    adoption = Adoption.objects.create(
        pet=pet,
        adopter=adopter,
        shelter=shelter,
        status="PENDING",
        adoption_data=timezone.now(),
    )

    assert adoption.id is not None  # type: ignore
    assert adoption.status == "PENDING"
    assert adoption.pet.name == "Amora"
