from django.db import models

class Order(models.Model):
    nr = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.nr}'