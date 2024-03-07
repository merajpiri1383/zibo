from django.urls import path 
from product import views
urlpatterns = [
    path("c/",views.CreateListCategoryAPIView.as_view()),
    path("c/<pk>/",views.CategoryAPIView.as_view()),
    path("",views.CreateListProductAPIView.as_view()),
    path("<pk>/",views.ProductAPIView.as_view()),
]  