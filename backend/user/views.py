from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.serializers import RegisterationSerializer,UserSerializer
from django.contrib.auth import get_user_model
from user.send_email import send_email
@api_view(["POST"])
def register_api_view(request) :
    serializer = RegisterationSerializer(data=request.data)
    if serializer.is_valid() :
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        send_email(user,request)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view()
def activate_email_api_view(request,code):
    try : user = get_user_model().objects.get(activation_code=code)
    except : return Response(data={"detail":"invalid code "},status=status.HTTP_400_BAD_REQUEST)
    user.is_active = True
    user.save()
    return Response(data=UserSerializer(user).data)