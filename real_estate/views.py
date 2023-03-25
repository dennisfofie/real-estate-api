from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import status, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from real_estate.serializer import (
    RegisterSerializer,
    LoginSerializer,
    UserSearializer,
    RefreshtokenSerializer,
)
from real_estate.models import User
from real_estate.token import generate_token

# Create your views here.


class RegisterUserView(APIView):
    serializer_classs = RegisterSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_classs(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "message": "Account created successfully",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogInUserView(APIView):
    serializer_class = LoginSerializer

    def post(self, request: Request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            token = generate_token(user)
            login(request, user)
            response = {"message": "Login successfully", "tokens": token}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data="Invalid email / password, try again")


class LogOutUserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RefreshtokenSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {"message": "Logout successfully"}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserListCreateView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = UserSearializer
    queryset = User.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRetrieveUpdateDestroy(
    generics.GenericAPIView,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = UserSearializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
