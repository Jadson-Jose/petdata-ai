from django.db import models


class Shelter(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    capacity = models.PositiveIntegerField(help_text="Capacidade máxima de animais.")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city}/{self.state}"
