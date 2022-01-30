from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class PetViewset(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','breed','gender','age','size']

class AnimalShelterViewset(viewsets.ModelViewSet):
    queryset = AnimalShelter.objects.all()
    serializer_class = AnimalShelterSerializer


