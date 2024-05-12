from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Product')
    model = models.CharField(max_length=50, verbose_name='Model')
    date = models.DateField(verbose_name="Date of start sales")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
