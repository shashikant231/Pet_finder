from .views import *
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register("pet_api",PetViewset,basename='pet_api')
router.register("animal_shelter_api",AnimalShelterViewset,basename='animal_shelter_api')

urlpatterns = [
    path('',include(router.urls)),
]
