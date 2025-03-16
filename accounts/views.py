from rest_framework import status

# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import (
    UpdatePasswordSerializer,
    UserSerializer,
)


class RegisterView(APIView):
    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MeView(APIView):
    #    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)


class UpdatePasswordView(APIView):
    #    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(request):
        serializer = UpdatePasswordSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
