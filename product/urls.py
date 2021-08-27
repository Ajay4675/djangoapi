from django.urls import include, path
from rest_framework import routers
from .import views

app_name = 'mastersindia'

router = routers.DefaultRouter()
router.register(r'category', views.CategoryAllSerializerView)
router.register(r'subcategory', views.SubCategorySerializerView)
router.register(r'product', views.ProductSerializerView)

urlpatterns = [
    path('', include(router.urls)),
]

