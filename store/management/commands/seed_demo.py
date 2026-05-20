import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from accounts.models import Account, UserProfile
from category.models import Category
from store.models import Product, Variation


class Command(BaseCommand):
    help = "Create demo furniture categories, products, variations, admin and customer accounts."

    def handle(self, *args, **options):
        source_dir = Path(settings.BASE_DIR) / "InteriorsSymphony" / "static" / "images" / "MEUBLES"
        media_dir = Path(settings.MEDIA_ROOT) / "photos" / "products"
        media_dir.mkdir(parents=True, exist_ok=True)

        categories = {
            "canapes": "Canapes",
            "tables": "Tables",
            "chaises": "Chaises",
            "decorations": "Decorations",
        }
        category_objects = {}
        for slug, name in categories.items():
            category_objects[slug], _ = Category.objects.get_or_create(
                slug=slug,
                defaults={
                    "category_name": name,
                    "description": f"Selection de {name.lower()} pour la maison.",
                },
            )

        products = [
            ("Canape nordique beige", "canapes", "1.jpg", 749, 12, "Canape confortable trois places pour salon moderne."),
            ("Canape velours noir", "canapes", "2.jpg", 899, 8, "Canape elegant en velours avec assise profonde."),
            ("Table basse bois clair", "tables", "3.jpg", 249, 20, "Table basse minimaliste en bois clair."),
            ("Table a manger familiale", "tables", "4.jpg", 599, 10, "Grande table pour salle a manger conviviale."),
            ("Chaise scandinave", "chaises", "5.jpg", 129, 35, "Chaise legere avec pieds bois et assise confortable."),
            ("Fauteuil lounge", "chaises", "6.jpg", 329, 14, "Fauteuil relax pour coin lecture ou salon."),
            ("Lampe design", "decorations", "7.jpg", 89, 40, "Lampe decorative pour ambiance chaleureuse."),
            ("Meuble TV contemporain", "decorations", "8.jpg", 479, 9, "Meuble TV bas avec rangements pratiques."),
        ]

        for name, category_slug, image_name, price, stock, description in products:
            source = source_dir / image_name
            target = media_dir / image_name
            if source.exists() and not target.exists():
                shutil.copy2(source, target)
            product, _ = Product.objects.update_or_create(
                slug=name.lower().replace(" ", "-"),
                defaults={
                    "product_name": name,
                    "description": description,
                    "price": price,
                    "stock": stock,
                    "is_available": True,
                    "category": category_objects[category_slug],
                    "images": f"photos/products/{image_name}",
                },
            )
            for color in ["beige", "noir", "blanc"]:
                Variation.objects.get_or_create(
                    product=product,
                    variation_category="color",
                    variation_value=color,
                    defaults={"is_active": True},
                )
            for size in ["standard", "grand"]:
                Variation.objects.get_or_create(
                    product=product,
                    variation_category="size",
                    variation_value=size,
                    defaults={"is_active": True},
                )

        client, created = Account.objects.get_or_create(
            email="client@myhouse.test",
            defaults={
                "first_name": "Client",
                "last_name": "Demo",
                "username": "client",
                "phone_number": "0600000001",
                "is_active": True,
            },
        )
        if created:
            client.set_password("123456")
            client.save()
        UserProfile.objects.get_or_create(user=client)

        admin, created = Account.objects.get_or_create(
            email="admin@myhouse.test",
            defaults={
                "first_name": "Admin",
                "last_name": "MyHouse",
                "username": "admin",
                "phone_number": "0600000000",
                "is_active": True,
                "is_staff": True,
                "is_admin": True,
                "is_superadmin": True,
            },
        )
        if created:
            admin.set_password("admin123")
            admin.save()
        UserProfile.objects.get_or_create(user=admin)

        self.stdout.write(self.style.SUCCESS("Demo data ready."))
