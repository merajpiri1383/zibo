from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from product.models import Product,Category
from product.serializers import CategorySerializer,ProductSerializer
class CreateListCategoryAPIView(APIView): 
    def post(self,request) : 
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CategoryAPIView(APIView) : 
    pass
class ProductAPIView : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
class CreateListProductAPIView(ProductAPIView,ListCreateAPIView) : 
    pass 
class ProductAPIView(ProductAPIView,RetrieveUpdateDestroyAPIView) : 
    pass 