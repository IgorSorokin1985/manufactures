from django.db import models
from products.models import Product

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Producer(models.Model):
    TYPE = (
        ("F", "Factory"),
        ("R", "Retail"),
        ("E", "Entrepreneur"),
    )
    name = models.CharField(max_length=50, verbose_name='Producer')
    type = models.CharField(max_length=1, choices=TYPE, verbose_name='Type')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Country')
    city = models.CharField(max_length=50, verbose_name='City')
    street = models.CharField(max_length=50, verbose_name='Street')
    number_home = models.PositiveIntegerField(verbose_name="Number of home")
    provider = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL)
    debt = models.IntegerField(verbose_name="Debt")
    date = models.DateField(auto_now_add=True, editable=False)
    products = models.ManyToManyField(Product, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'
