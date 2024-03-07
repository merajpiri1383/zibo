from django.db import models
from django.utils.text import slugify
class Category(models.Model) : 
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="categories/images")
    def __str__(self): 
        return self.name
class Product(models.Model): 
    name = models.CharField(max_length=200,db_index=True,unique=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/images")
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name="products")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self) : 
        return f"{self.name} : {self.price}"