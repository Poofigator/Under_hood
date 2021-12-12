from rest_framework import viewsets

from .serialaizers import CarSerializer
from ..models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        res = Car.objects.filter(number=self.request.query_params.get('number'))
        return res

    def perform_create(self, CarSerializer):
        res = Car.objects.filter(number=self.request.data.get('number'))
        if res:
            res.delete()
        if self.request.data.get('place') != 'Выход':
            CarSerializer.save(number=self.request.data.get('number'))

