from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class PetViewset(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class AnimalShelterViewset(viewsets.ModelViewSet):
    queryset = AnimalShelter.objects.all()
    serializer_class = AnimalShelterSerializer


