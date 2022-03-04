from django.db import models

# Create your models here.
class Toy(models.Model):
    value = models.CharField(max_length=200)


class Stock(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return super().__str__()