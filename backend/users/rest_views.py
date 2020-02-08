from django.contrib.auth import login
from django.conf import settings

from rest_framework import serializers
from rest_framework.generics import (
  RetrieveAPIView, UpdateAPIView
)
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
  AllowAny, IsAuthenticated)
from rest_framework.response import Response

from users.models import User, MagicLink
from users.serializers import (
  RetrieveUserExistsSerializer, RetrieveCurrentUserSerializer,
  UpdateUserPasswordSerializer, RetrieveMagicLinkSerializer
)


class RetrieveUserExistsView(RetrieveAPIView):
  lookup_field = 'email'
  permission_classes = (AllowAny, )
  queryset = User.objects.all()
  serializer_class = RetrieveUserExistsSerializer


class RetrieveCurrentUserView(RetrieveAPIView):
  lookup_field = None
  permission_classes = (IsAuthenticated, )
  serializer_class = RetrieveCurrentUserSerializer

  def get_object(self):
    return self.request.user

class UpdateUserPasswordView(UpdateAPIView):
  allowed_methods = ('PUT', )
  lookup_field = None
  permission_classes = (IsAuthenticated, )
  serializer_class = UpdateUserPasswordSerializer

  def get_object(self):
    return self.request.user

  def perform_update(self, serializer):
    user = self.request.user
    user.set_password(serializer['password'])


class RetrieveMagicLinkView(RetrieveAPIView):
  permission_classes = (AllowAny, )
  serializer_class = RetrieveMagicLinkSerializer
  queryset = MagicLink.objects.active()

  def retrieve(self, *args, **kwargs):
    instance = self.get_object()
    user = instance.user
    login(
      self.request, user,
      backend=settings.AUTHENTICATION_BACKENDS[0]
    )
    response_data = self.serializer_class(instance).data
    instance.delete()
    return Response(response_data)