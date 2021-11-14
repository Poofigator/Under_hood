from django.db import models


class Car(models.Model):
    number = models.CharField(max_length=12)
    place = models.CharField(max_length=255)

    def __str__(self):
        return  "Машина с номером {} находится на {}".format(self.number, self.place)
