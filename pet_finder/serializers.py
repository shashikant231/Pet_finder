from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
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
        res['contact_no'] = AnimalShelter.objects.filter(id = animal_id).values('contact_no')[0]['contact_no']
        user_id = AnimalShelter.objects.filter(id=animal_id).values('user')[0]['user']
        res['user_email'] = User.objects.filter(id = user_id).values('email')[0]['email']
        print(user_id)

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
        resp = super().to_representation(instance)
        user_info_id = resp['user_info_id']
        user_id = resp['user_id']
        animal_shelter_id = resp['animal_shelter_id']
        # print(animal_shelter_id)
        pet_id = resp['pet']
        resp['user_email'] = User.objects.filter(id = user_id).values('email')[0]['email']
        resp['phone_number'] = UserInfo.objects.filter(id = user_info_id).values('phone_number')[0]['phone_number']
        resp['user_pincode'] = UserInfo.objects.filter(id = user_info_id).values('pincode')[0]['pincode']
        resp['user_state'] = UserInfo.objects.filter(id = user_info_id).values('state')[0]['state']
        resp['user_city'] = UserInfo.objects.filter(id = user_info_id).values('city')[0]['city']
        resp['customer_pic'] = "http://127.0.0.1:8000/media/" + UserInfo.objects.filter(id=user_info_id).values('profile_pic')[0]['profile_pic']
        resp['customer_name'] = UserInfo.objects.filter(id=user_info_id).values('first_name')[0]['first_name']
        resp['animal_shelter_pic'] = "http://127.0.0.1:8000/media/" + AnimalShelter.objects.filter(id=animal_shelter_id).values('profile_pic')[0]['profile_pic']
        resp['animal_shelter_name'] = AnimalShelter.objects.filter(id=animal_shelter_id).values('organisations_name')[0]['organisations_name']
        resp['pet_name'] = Pet.objects.filter(id=pet_id).values('name')[0]['name']


        return resp