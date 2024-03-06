from django.urls import path
from user import views
urlpatterns = [
    path("register/",views.register_api_view,name="register"),
    path("activate/",views.activate_email_api_view,name="activate"),
    path("login/",views.login_api_view,name="login"),
    path("password/reset/<email>/",views.RestPasswordAPIView.as_view()),
] 