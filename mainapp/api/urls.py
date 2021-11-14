from rest_framework import routers

from .views import CarViewSet

router = routers.SimpleRouter()

router.register('car', CarViewSet, basename='car-base')

urlpatterns = []
urlpatterns += router.urls
