from rest_framework import viewsets

from .serialaizers import CarSerializer
from ..models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        res = Car.objects.filter(number=self.request.query_params.get('number'))
        return res
