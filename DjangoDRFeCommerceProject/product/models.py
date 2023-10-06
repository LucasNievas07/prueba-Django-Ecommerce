from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    # Define the natural order of the data
    class MPTTMeta:
        order_insertion_by = ["name"]

    # Returns data from the table
    def __str__(self):
        return self.name


class Brand(MPTTModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(MPTTModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # It is not necessary to add a description
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
