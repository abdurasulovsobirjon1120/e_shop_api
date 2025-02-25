from rest_framework import serializers
from .models import CustomUser, BaseUserManager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class LoginStartSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ('phone', 'password')
        
class LoginEndSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()
    code_token = serializers.CharField()