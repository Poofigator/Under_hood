from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from mainapp.models import Car


class Command(BaseCommand):
    help = 'Deletes expired rows'

    def handle(self, *args, **options):
        for obj in Car.objects.all():
            obj_time = obj._meta.get_field('add_date').value_from_object(Car.objects.first())
            if timezone.now() > obj_time + timedelta(hours=24):
                obj.delete()

