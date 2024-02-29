from django.db import models

class Order(models.Model):
    nr = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', null=True)


    def __str__(self) -> str:
        return f'{self.nr}'