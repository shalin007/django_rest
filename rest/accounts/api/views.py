from django.contrib.auth import authenticate,get_user_model
from django.db.models import Q
from rest_framework import permissions,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import jwt_response_payload_handler

from .serializers import UserRegisterSerializer

from .permissions import AnonPermission


User=get_user_model()


from rest_framework_jwt.settings import api_settings

jwt_payload_handler             =   api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              =   api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    =   api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class AuthView(APIView):
    permission_classes      = [permissions.AllowAny]
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return Response({'detail':'you are already authenticated'})
        data=request.data
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()
        if qs.count()==1:
            user_obj=qs.first()
            if user_obj.check_password(password):
                user=user_obj
                payload =jwt_payload_handler(user)
                token   = jwt_encode_handler(payload)
                response= jwt_response_payload_handler(token,user,request)
                return Response(response)
        return Response({"detail":"invslid"})

class RegisterAPIView(generics.CreateAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserRegisterSerializer
    permission_classes  = [AnonPermission]



#
# class RegisterAPIView(APIView):
#     permission_classes      = [permissions.AllowAny]
#     def post(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return Response({'detail':'you are already authenticated'})
#         data          = request.data
#         username      = data.get('username')
#         email         = data.get('email')
#         password      = data.get('password')
#         password2     = data.get('password2')
#         qs = User.objects.filter(
#             Q(username__iexact=username)|
#             Q(email__iexact=email)
#         )
#         if password2!= password:
#             return Response({"password":"password must match"})
#         if qs.exists():
#             return Response({"detail":"user already exists"})
#         else:
#             user=User.objects.create(username=username,email=email)
#             user.set_password(password)
#             user.save()
#             # if user_obj.check_password(password):
#             #     user=user_obj
#             #     payload =jwt_payload_handler(user)
#             #     token   = jwt_encode_handler(payload)
#             #     response= jwt_response_payload_handler(token,user,request)
#             return Response({"detail":"thank you!"})
#         return Response({"detail":"invslid request"})