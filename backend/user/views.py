from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.serializers import RegisterationSerializer,UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import regex
from user.send_email import send_email,send_password_reset_email
@api_view(["POST"])
def register_api_view(request) :
    serializer = RegisterationSerializer(data=request.data)
    if serializer.is_valid() :
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        send_email(user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"]) 
def activate_email_api_view(request):
    try :
        user = get_user_model().objects.get(email=request.data.get("email"))
    except :
        return Response(data={"detail":"invalid email address ."},status=status.HTTP_400_BAD_REQUEST)
    try : code = request.data.get("code")
    except : return Response({"detail":"code is required ."},status=status.HTTP_400_BAD_REQUEST)
    if user.activation_code == code :
        user.is_active = True
        user.save()
        data = UserSerializer(user).data
        token = RefreshToken.for_user(user)
        data["access_token"] = str(token.access_token)
        data["refresh_token"] = str(token)
        return Response(data=data)
    return Response(data={"detail":"invalid code"},status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def login_api_view(request) :
    try :
        user = get_user_model().objects.get(email=request.data['email'])
    except :
        return Response(data={"detail":"invalid email"},status=status.HTTP_400_BAD_REQUEST)
    if not request.data.get("password") :
        return Response(data={"detail":"password is required ."},status=status.HTTP_400_BAD_REQUEST)
    if not user.check_password(request.data['password']) :
        return Response(data={"detail":"password or email is wrong"},status=status.HTTP_400_BAD_REQUEST)
    data = UserSerializer(user).data
    user = RefreshToken.for_user(user)
    data["access_token"] = str(user.access_token)
    data["refresh_token"] = str(user)
    return Response(data=data)
class RestPasswordAPIView(APIView): 
    def get(self,request,email): 
        try : user = get_user_model().objects.get(email=email)
        except : return Response(data={"detail":"invalid email address"},status=status.HTTP_400_BAD_REQUEST)
        send_password_reset_email(user=user)
        return Response(data={"data":"code sent ."})
    def post(self,request,email):
        try : user = get_user_model().objects.get(email=email)
        except : return Response(data={"detail":"invalid email address"},status=status.HTTP_400_BAD_REQUEST)
        if not request.data.get("code") : return Response(data={"detail":"code is required ."},status=status.HTTP_400_BAD_REQUEST)
        if request.data.get("code") != user.activation_code : 
            return Response(data={"detail":"invalid code "},status=status.HTTP_400_BAD_REQUEST)
        if not request.data.get("password") : return Response(data={"detail":"password required "},status=status.HTTP_400_BAD_REQUEST)
        if not regex.findall(request.data.get("password")) :
            return Response(
                data={"detail":"your password must contain at least one uppercase letter and one @#$% and at least 8 character"},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(request.data.get("password"))
        user.save()
        return Response(data=UserSerializer(user).data)