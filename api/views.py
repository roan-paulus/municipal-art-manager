from django.contrib.auth.models import User, Group
from .models import OverheidsGebouw, Kamer, Artiest, Kunstwerk
from .serializers import (
    OverheidsGebouwSerializer,
    KamerSerializer,
    ArtiestSerializer,
    KunstwerkSerializer
)
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class OverheidsGebouwViewSet(viewsets.ModelViewSet):
    queryset = OverheidsGebouw.objects.all()
    serializer_class = OverheidsGebouwSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KamerViewSet(viewsets.ModelViewSet):
    queryset = Kamer.objects.all()
    serializer_class = KamerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArtiestViewSet(viewsets.ModelViewSet):
    queryset = Artiest.objects.all()
    serializer_class = ArtiestSerializer
    permission_classes = [permissions.IsAuthenticated]


class KunstwerkViewSet(viewsets.ModelViewSet):
    queryset = Kunstwerk.objects.all()
    serializer_class = KunstwerkSerializer
    permission_classes = [permissions.IsAuthenticated]

