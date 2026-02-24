import pytest

from apps.adopters.models import Adopter


@pytest.mark.django_db
def test_create_adopter():
    adopter = Adopter.objects.create(
        full_name="Jadson Silva",
        email="jadson@email.com",
        phone="11988887777",
        city="São Paulo",
        state="SP",
    )

    assert adopter.id is not None
    assert adopter.is_active is True
    assert adopter.city == "São Paulo"
