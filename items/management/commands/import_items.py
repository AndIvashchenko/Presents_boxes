import requests
from django.core.management import BaseCommand

from items.models import Item


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://stepik.org/media/attachments/course/73594/presentsboxes.json')
        response.raise_for_status()

        for item in response.json():
            Item.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item['title'],
                    'description': item['description'],
                    'image': '',
                    'weight': item['weight_grams'],
                    'price': item['price'],
                }
            )
