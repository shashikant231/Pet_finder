from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Pet)
admin.site.register(AnimalShelter)
admin.site.register(AdoptionForm)

