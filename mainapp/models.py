from django.db import models


class Car(models.Model):
    number = models.CharField(max_length=12)
    place = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Машина с номером {} находится на {}, время добавления записи - {}".format(self.number, self.place, self.add_date)
