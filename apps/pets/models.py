from django.db import models

from apps.shelters.models import Shelter


class Pet(models.Model):
    class Species(models.TextChoices):
        DOG = "DOG", "Dog"
        CAT = "CAT", "Cat"

    class Size(models.TextChoices):
        SMALL = "SMALL", "Small"
        MEDIUM = "MEDIUM", "Medium"
        LARGE = "LARGE", "Large"

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    name = models.CharField(max_length=100)

    species = models.CharField(
        max_length=10,
        choices=Species.choices,
    )

    age = models.PositiveIntegerField(help_text="Idade em anos")

    size = models.CharField(
        max_length=10,
        choices=Size.choices,
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
    )

    is_adopted = models.BooleanField(default=True)

    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name="pets")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
