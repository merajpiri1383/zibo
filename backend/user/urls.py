from django.urls import path
from user import views
urlpatterns = [
    path("register/",views.register_api_view),
    path("activate/<slug:code>/",views.activate_email_api_view,name="activate"),
]