from django.db import models


class Product(models.Model):
    external_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)

    rating_rate = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    rating_count = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.external_id})"
