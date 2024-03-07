from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response 
from rest_framework import status 
from product.models import Product,Category
from product.serializers import CategorySerializer,ProductSerializer
class CategoryAPI:
    queryset = Category.objects.all()
    http_method_names = ["get","post"]
    serializer_class = CategorySerializer
class CreateListCategoryAPIView(CategoryAPI,ListCreateAPIView):  
    pass
class CategoryAPIView(CategoryAPI,RetrieveUpdateDestroyAPIView) : 
    http_method_names = ["get","put","delete"]
class ProductAPI : 
    http_method_names = ["get","post"]
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
class CreateListProductAPIView(ProductAPI,ListCreateAPIView) : 
    serializer_class = ProductSerializer
class ProductAPIView(ProductAPI,RetrieveUpdateDestroyAPIView):
    http_method_names = ["get","put","delete"]