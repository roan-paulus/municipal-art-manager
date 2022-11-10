from django.contrib.auth.models import User, Group
from .models import OverheidsGebouw, Kamer, Artiest, Kunstwerk
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OverheidsGebouwSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OverheidsGebouw
        fields = ["adres", "postcode", "stad", "pand_code"]


class KamerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kamer
        fields = ["verdieping", "kamer_identificatie", "gebouw"]


class ArtiestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artiest
        fields = ["naam"]


class KunstwerkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kunstwerk
        fields = [
            "titel"
            "artiesten",
            "beschrijving",
            "locatie",
            "lengte",
            "breedte",
            "hoogte",
        ]

