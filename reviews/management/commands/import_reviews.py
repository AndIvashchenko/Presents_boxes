from datetime import datetime

import requests
from django.core.management import BaseCommand

from reviews.models import Review
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json')
        response.raise_for_status()

        for review in response.json():
            author = User.objects.get(id=review['author'])
            if review['published_at']:
                print('jghjghjhg')
                date = datetime.strptime(review['published_at'], "%Y-%m-%d"),
            else:
                date = None
            Review.objects.update_or_create(
                id=review['id'],
                author=author,
                defaults={
                    'text': review['content'],
                    'created_at': datetime.strptime(review['created_at'], "%Y-%m-%d"),
                    'published_at': date,
                    'status': review['status'],
                }
            )
