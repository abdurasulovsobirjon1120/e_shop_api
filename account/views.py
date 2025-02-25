from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, BaseUserManager, CodeConfirmation
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from e_shop_api.helpers.generatecode import *
from e_shop_api.helpers.sms import *

class RegisterApiView(APIView):
    # permission_class = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        
        ex_user = CustomUser.objects.filter(email=email).first()
        if ex_user:
            return Response( {'message':'Bu raqam tizimda allaqachon mavjud'})
        user = CustomUser.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password),
            is_active=True
        )
        token = RefreshToken.for_user(user)
        return Response({
            'message':'Success',
            'user': UserSerializer(user).data,
            'access_token':str(token.access_token),
            'refresh_token':str(token)
        })
               
class LoginAPIView(APIView):
    # permission_class = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        ex_user = CustomUser.objects.filter(email=email).first()
        
        if not ex_user:
            return Response({'massage' : 'Bu Email tizimda mavjud emas'})
        
        code = generate_code(5)
        code_token = generate_code_token(32)
        sms = send_email(code, email)
        
        ex = CodeConfirmation.objects.create(
            user = ex_user,
            code = code,
            code_token = code_token
        )
        
        
        return Response(
            {
                'message':str(sms['message']),                
                "Code" : str(code_token)
            }
        )
        
class LoginEndAPIView(APIView):
    def post(self, request):
        code = int(request.data.get('code'))
        code_token = request.data.get('code_token')
        
        ex_confirmation = CodeConfirmation.objects.filter(code=code, code_token=code_token).first()
        print(ex_confirmation)
        
        if not ex_confirmation:
            return Response({'massage' : 'Wrong code!'}) 
        token = RefreshToken.for_user(ex_confirmation.user)
        ex_confirmation.delete()
        return Response({
            'message':'Success',
            'access_token':str(token.access_token),
            'refresh_token':str(token)
        })