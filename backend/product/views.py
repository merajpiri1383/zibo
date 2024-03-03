from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from product.models import Product,Category
from product.serializers import CategorySerializer,ProductSerializer
class CategoryAPIView : 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CreateListCategoryAPIView(CategoryAPIView,ListCreateAPIView): 
    pass 
class CategoryAPIView(CategoryAPIView,RetrieveUpdateDestroyAPIView) : 
    pass 
class ProductAPIView : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
class CreateListProductAPIView(ProductAPIView,ListCreateAPIView) : 
    pass 
class ProductAPIView(ProductAPIView,RetrieveUpdateDestroyAPIView) : 
    pass 