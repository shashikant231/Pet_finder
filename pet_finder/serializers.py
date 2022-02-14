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
        animal_id = res['animalshelter']
        animal_name = AnimalShelter.objects.filter(id=animal_id).values('organisations_name')
        res['pincode'] = AnimalShelter.objects.filter(id = animal_id).values('pincode')[0]['pincode']
        res['state'] = AnimalShelter.objects.filter(id = animal_id).values('state')[0]['state']
        res['city'] = AnimalShelter.objects.filter(id = animal_id).values('city')[0]['city']
        res['animal_shelter_name'] = animal_name[0]['organisations_name']
        return res

class AnimalShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalShelter
        fields = "__all__"

class AdoptionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionForm
        fields = "__all__"

        # AnimalShelter.objects.filter(id=animal_id).values('organisations_name')
    def to_representation(self, instance):
        print(instance)
        resp = super().to_representation(instance)
        animal_sheler_id = resp['send_form_to']
        resp['pincode'] = AnimalShelter.objects.filter(id = animal_sheler_id).values('pincode')[0]['pincode']
        resp['state'] = AnimalShelter.objects.filter(id = animal_sheler_id).values('state')[0]['state']
        resp['city'] = AnimalShelter.objects.filter(id = animal_sheler_id).values('city')[0]['city']
        return resp