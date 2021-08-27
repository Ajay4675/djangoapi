from .serializers import * 
from rest_framework import viewsets

class CategoryAllSerializerView(viewsets.ModelViewSet):  
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SubCategorySerializerView(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.filter()
    def get_queryset(self):
        category = self.request.query_params.get('category')
        queryset = SubCategory.objects.filter()
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class ProductSerializerView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    def get_queryset(self):
        category = self.request.query_params.get('category')
        subcategory = self.request.query_params.get('subcategory')
        queryset = Product.objects.filter()
        if category:
            queryset = queryset.filter(subcategory__category=category)
        elif subcategory:
            queryset = queryset.filter(subcategory=subcategory)
        return queryset

