import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from inventory.models import Inventory

class Command(BaseCommand):
    help = "Seed the database with sample product data."

    def handle(self, *args, **options):
        # Path to your image in static files
        image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'test_shirt.jpg')

        if not os.path.exists(image_path):
            self.stdout.write(self.style.ERROR("Image file not found."))
            return

        with open(image_path, 'rb') as img_file:
            image_file = File(img_file)

            # Create sample shirts
            for i in range(5):
                product = Inventory(
                    name=f"Test Shirt {i + 1}",
                    description="A high-quality test shirt for demo purposes.",
                    product_type="Shirt",
                    price=19.99,
                    inventory=20,
                    size="L",
                    color="Black"
                )
                product.image.save(f"test_shirt_{i + 1}.jpg", image_file)
                product.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded test shirt products."))
