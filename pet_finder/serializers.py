from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

class AnimalShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalShelter
        fields = "__all__"