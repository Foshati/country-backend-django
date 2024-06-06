from django.db import models
from cities_light.models import Country, City


class Address(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    street_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"
