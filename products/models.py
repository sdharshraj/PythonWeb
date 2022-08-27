from django.db import models

# standard max length for urls 2083

class Product(models.Model) :
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offers(models.Model) :
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    discount = models.FloatField()
