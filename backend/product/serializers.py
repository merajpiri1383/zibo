from rest_framework import serializers 
from product.models import Category,Product
class CategoryWithoutProductSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Category 
        fields = ["id","name"]
class ProductSerializer(serializers.ModelSerializer) : 
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True
    )
    class Meta : 
        model = Product 
        fields = ["id","name","price","image","created","category","description"]
class CategorySerializer(serializers.ModelSerializer) : 
    products = ProductSerializer(
        instance=Product.objects.all(),
        many=True,
        required=False
    )
    class Meta : 
        model = Category 
        fields = ["id","name","products"]