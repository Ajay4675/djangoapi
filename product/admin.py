from .models import Category, SubCategory, Product
from django.contrib import admin

# Register your models here.
admin.site.register(Category)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'sub_category_name' )

admin.site.register(SubCategory, SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'product_name',)

admin.site.register(Product, ProductAdmin)