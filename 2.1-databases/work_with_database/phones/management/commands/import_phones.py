import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                id=int(phone['id']),
                name=phone['name'],
                image=phone['image'],
                price=int(phone['price']),
                release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                lte_exists=True if phone['lte_exists'] == 'True' else False,
                slug=slugify(phone['name']),
                                )
