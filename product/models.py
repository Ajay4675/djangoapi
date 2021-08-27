from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="categorys", on_delete=models.PROTECT)
    sub_category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.sub_category_name

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=150)
    def __str__(self):
        return self.product_name
