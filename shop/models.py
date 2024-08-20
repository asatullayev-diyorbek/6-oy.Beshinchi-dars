from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

