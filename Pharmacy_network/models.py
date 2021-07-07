from django.db import models


class Pharmacy(models.Model):
    name = models.TextField()
    address = models.TextField()
    open_date = models.TimeField()
    close_date = models.TimeField()

    def __str__(self):
        return self.name


class Stuff(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    country = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Pharmacy_staff(models.Model):
    stuff = models.ForeignKey(
        Stuff,
        on_delete=models.CASCADE,
    )
    pharmacy = models.ForeignKey(
        Pharmacy,
        on_delete=models.CASCADE,
    )