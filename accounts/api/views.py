from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)


User = get_user_model()

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data

            from django.contrib.auth import login, authenticate

            print("--------------------------------")
            print(dict(data.lists()))
            data = dict(data.lists())

            from rest_framework.authentication import SessionAuthentication, BasicAuthentication
            from rest_framework.permissions import IsAuthenticated
            from rest_framework.response import Response
            from rest_framework.views import APIView

            authentication_classes = (SessionAuthentication, BasicAuthentication)
            permission_classes = (IsAuthenticated,)

            def get(self, request, format=None):
                content = {
                    'user': unicode(request.user),  # `django.contrib.auth.User` instance.
                    'auth': unicode(request.auth),  # None
                }
                return Response(content)
                return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





