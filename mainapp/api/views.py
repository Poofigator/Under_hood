from rest_framework import viewsets

from .serialaizers import CarSerializer
from ..models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(**self.request.data)

    def get_queryset(self):
        return Car.objects.filter(number=self.request.data.get('number'))
