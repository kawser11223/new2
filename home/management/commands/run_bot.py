from django.core.management.base import BaseCommand
from home.telegram_bot import run_bot 

class Command(BaseCommand):
    help = 'Run the telegram bot'

    def handle(self, *args, **options):
        run_bot()
