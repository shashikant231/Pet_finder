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

    def to_representation(self, instance):
        res = super().to_representation(instance)
        animal_id = res['animal_shelter']
        animal_name = AnimalShelter.objects.filter(id=animal_id).values('organisations_name')
        res['animal_shelter_name'] = animal_name[0]['organisations_name']
        return res

class AnimalShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalShelter
        fields = "__all__"