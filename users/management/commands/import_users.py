import requests
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json')
        response.raise_for_status()

        for user in response.json():
            User.objects.update_or_create(
                id=user['id'],
                defaults={
                    'username': user['email'].split('@')[0],
                    'email': user['email'],
                    'password': user['password'],
                    'first_name': user['info']['name'],
                    'middle_name': user['info']['patronymic'],
                    'last_name': user['info']['surname'],
                    'phone': user['contacts']['phoneNumber'],
                    'address': user['city_kladr'],
                    'type_account': user['premium'],
                }
            )
