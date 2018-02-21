from django.db import models


# Create your models here.
class Product():
    product_name = models.TextField(null=True, blank=True)
    product_price = models.TextField(null=True, blank=True)
    product_desc = models.TextField(null=True, blank=True)


class Category():
    cat_name = models.TextField(null=True, blank=True)
    cat_desc = models.TextField(null=True, blank=True)
