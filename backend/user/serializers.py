from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
regex = re.compile(r"(?=.*[0-9])(?=.*[A-Z])(?=.*)(?=.*[@|#|$|%]).{8,16}")
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = get_user_model()
        fields = ["id","email","is_active","is_superuser","is_staff"]
class RegisterationSerializer(serializers.ModelSerializer):
    class Meta :
        model = get_user_model()
        fields = ["id","email","password"]
    def validate(self,data):
        password = data.get("password")
        if not regex.findall(password) :
            raise serializers.ValidationError(
                """your password must contain at least one uppercase letter and one @#$% and at least 8 character""")
        return data