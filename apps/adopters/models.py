from django.db import models


class Adopter(models.Model):
    full_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
