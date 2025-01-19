from django.db import models

# Create your models here.

from django.db import models

class Endpoint(models.Model):
    name = models.CharField(max_length=200, help_text="Имя эндпоинта")
    url = models.CharField(max_length=200, help_text="URL эндпоинта")
    description = models.TextField(blank=True, help_text="Описание функциональности эндпоинта")
    method = models.CharField(
        max_length=10,
        choices=[
            ("GET", "GET"),
            ("POST", "POST"),
            ("PUT", "PUT"),
            ("DELETE", "DELETE"),
            ("PATCH", "PATCH")
        ],
        help_text="HTTP метод"
    )

    def __str__(self):
        return f"{self.method} {self.url} - {self.name}"
