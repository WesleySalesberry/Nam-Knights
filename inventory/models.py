from django.db import models

class Inventory(models.Model):
    PRODUCT_TYPES = [
        ("Shirt", "Shirt"),
        ("Coin", "Coin"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default="Shirt")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    available = models.BooleanField(default=True)
    size = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="Size (e.g., S, M, L, XL). Only for shirts."
    )
    color = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text="Color (optional). Only for shirts."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


