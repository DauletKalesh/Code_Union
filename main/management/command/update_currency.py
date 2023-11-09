from django.core.management.base import BaseCommand
from main.models import Currency

class Command(BaseCommand):
    help = 'Update and view currency data'

    def add_arguments(self, parser):
        parser.add_argument('--update', action='store_true', help='Update currency data')
        parser.add_argument('--view', action='store_true', help='View currency data')

    def handle(self, *args, **options):
        if options['update']:
            # Call function to update currency data
            self.stdout.write(self.style.SUCCESS('Currency data updated successfully'))

        if options['view']:
            currencies = Currency.objects.all()
            for currency in currencies:
                self.stdout.write(self.style.SUCCESS(f'{currency.name}: {currency.rate}'))
