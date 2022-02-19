from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings


# def send_email():
#     send_mail(
#         'Your enquiry has been received',
#         "hello",
#         settings.EMAIL_HOST_USER,
#         ['shashikantching@gmail.com',],
#         fail_silently=False,

#     )



# Create your views here.

class UserInfoViewset(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    # permission_classes = (IsAuthenticated,) 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id']

class PetViewset(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    # permission_classes = (IsAuthenticated,) 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','breed','gender','age','size','animalshelter__pincode']

class AnimalShelterViewset(viewsets.ModelViewSet):
    queryset = AnimalShelter.objects.all()
    serializer_class = AnimalShelterSerializer
    # permission_classes = (IsAuthenticated,) 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id']

class AdoptionFormViewset(viewsets.ModelViewSet):
    queryset = AdoptionForm.objects.all()
    serializer_class =AdoptionFormSerializer
    filter_backends = [DjangoFilterBackend]
    # permission_classes = (IsAuthenticated,) 
    filterset_fields = ['id','user_id__id','animal_shelter_id__id']


