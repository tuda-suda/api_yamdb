from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import YAMDB_NOREPLY_EMAIL
from .models import User
from .permissions import IsAdmin, IsModerator, IsOwner, ReadOnly
from .serializers import (EmailSignUpSerializer, CodeConfirmationSerializer, 
    UserSerializer)


class EmailSignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailSignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(email=email, is_active=False)
            
            user = get_object_or_404(User, email=email)
            confirmation_code = default_token_generator.make_token(user)
            send_mail(
                mail_subject='Код подтверждения',
                message=f'Ваш код подтверждения {confirmation_code}',
                from_email=YAMDB_NOREPLY_EMAIL,
                [email]
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CodeConfirmationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CodeConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            confirmation_code = serializer.data.get('confirmation_code')
            user = get_object_or_404(User, email=email)

            if default_token_generator.check_token(user, confirmation_code):
                token = AccessToken.for_user(user)
                return Response(
                    {'token': token},
                    status=status.HTTP_200_OK
                )
            return Response(
                {'confirmation_code': 'Неверный код подтеврждения'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class UserOwnView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

