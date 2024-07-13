# backend/coffeeShops/management/commands/add.py

from django.core.management.base import BaseCommand
from coffeeShops.models import CoffeeShop

class Command(BaseCommand):
    help = 'Add initial coffee shops'

    def __init__(self):
        print("Command add_coffee_shops loaded")
        super().__init__()

    def handle(self, *args, **kwargs):
        coffee_shops = [
            {'name': 'Coffee Shop 1', 'address': '123 Coffee St', 'latitude': 40.7128, 'longitude': -74.0060},
            {'name': 'Coffee Shop 2', 'address': '456 Java Ave', 'latitude': 34.0522, 'longitude': -118.2437},
            {'name': 'Coffee Shop 3', 'address': '789 Espresso Rd', 'latitude': 37.7749, 'longitude': -122.4194},
        ]

        for shop in coffee_shops:
            CoffeeShop.objects.create(**shop)

        self.stdout.write(self.style.SUCCESS('Successfully added coffee shops'))