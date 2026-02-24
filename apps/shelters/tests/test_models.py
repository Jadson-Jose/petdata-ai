import pytest

from apps.shelters.models import Shelter


@pytest.mark.django_db
def test_create_shelter():
    shelter = Shelter.objects.create(
        name="Abrigo Esperança",
        city="Campinas",
        state="SP",
        email="contato@abrigo.com",
        phone="19999999999",
        capacity=120,
    )

    assert shelter.id is not None  # type: ignore
    assert shelter.name == "Abrigo Esperança"
    assert shelter.city == "Campinas"
    assert shelter.capacity == 120
