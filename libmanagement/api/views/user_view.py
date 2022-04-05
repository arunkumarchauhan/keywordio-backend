from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from rest_framework_simplejwt.tokens import RefreshToken


import logging

from api.serializers import UserCreateSerializer


logger = logging.getLogger('django')
from rest_framework import decorators,permissions,response,request,status
from rest_framework.response import Response


from api.models import User

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
JWT_DECODE_HANDLER = api_settings.JWT_DECODE_HANDLER




class RegisterView(APIView):
    permission_classes = []
    authentication_class = []
    def post(self,request,type="student"):
        try:
            is_staff= True if type.upper()=="ADMIN" else False
            serializer = UserCreateSerializer(data={'is_staff':is_staff,**request.data})

            if not serializer.is_valid():
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return response.Response(res, status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    permission_classes = []  # (IsAuthenticated,)
    authentication_class = []  # JSONWebTokenAuthentication

    def post(self, request):
        try:
            try:
                email = request.data['email']
                password = request.data['password']
            except Exception as e:
                logger.exception(e)
                return Response({'error': 'Required data not provided'}, status=status.HTTP_400_BAD_REQUEST)
            user_list = User.objects.filter(email=email)
            if len(user_list) == 0:
                return Response({'error': 'Account with this email is not registered '},
                                status=status.HTTP_404_NOT_FOUND)
            user = authenticate(email=email, password=password)

            if user is None:
                return Response({'error': 'Incorrect password '}, status=status.HTTP_404_NOT_FOUND)
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)

            response_data = {
                'message': 'User logged in successfully',
                'token': jwt_token,
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
