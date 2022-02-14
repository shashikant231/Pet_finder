from django.db import models
from django.conf import settings
from django.utils import tree
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator)

from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    post_delete

)
from django.core.mail import send_mail
from django.conf import settings
import json



PHONE_HELP_TEXT = "For e.g +91-95544-95544, +91-12345-54321, etc."

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


# Create your models here.
class CommonFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractBaseUser, CommonFields,PermissionsMixin):
    CUSTOMER = "CUS"
    ANIMALSHELTER = "AS"
    USER_TYPES = (
        (CUSTOMER , "CUS"),
        (ANIMALSHELTER, "AS"),
    )
    user_type = models.CharField(max_length=3, choices=USER_TYPES, default="CUS")
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name',"user_type"]

    def __str__(self):
        return self.user_name


class AnimalShelter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="animal_name")
    organisations_name = models.CharField(max_length=100)
    contact_no = PhoneNumberField("Phone Number", help_text=PHONE_HELP_TEXT)
    pincode = models.IntegerField(
        "PIN code",
        help_text="6 digits [0-9] PIN code",
        validators=[MinValueValidator(100000), MaxValueValidator(999999)],
    )
    state = models.CharField(max_length=50,null=False)
    city = models.CharField(max_length=80,null=False)
    organisations_mission = models.TextField(null=True,blank=True)
    organisations_policies = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.organisations_name



class Pet(models.Model):
    name = models.CharField(max_length=100,blank=False)
    breed = models.CharField(max_length=30,blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    gender = models.CharField(choices=gender_choices, max_length=10)
    color = models.CharField(max_length=20,blank=True)
    age = models.CharField(max_length=30,blank=False)
    size_choices = (("Puppy", "Puppy"), ("Adult", "Adult"),("Medium","Medium"))
    size = models.CharField(choices=size_choices,max_length=10,blank=False)
    vaccination_choices = (("Not Vaccianted", "Not Vaccianted"), ("Partially Vaccinated", "Partially Vaccinated"),("Completely vaccinated","Completely Vaccinated"))
    vaccination = models.CharField(choices=vaccination_choices,max_length=30,blank=False)
    first_image = models.ImageField(upload_to ='media/')
    second_image = models.ImageField(upload_to ='media/',blank = True)
    third_image = models.ImageField(upload_to ='media/',blank = True)
    animalshelter = models.ForeignKey(AnimalShelter,on_delete=models.Case,related_name="pet_shelter")
    adoption_fee = models.PositiveIntegerField(blank=True)
    is_rescued = models.BooleanField(default=False)
    story = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return f"Name and Breed:{self.name} - {self.breed}"

class AdoptionForm(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE,related_name="adoption_form_user")
    send_form_to = models.ForeignKey(AnimalShelter,on_delete=models.CASCADE,related_name="adoption_form_to")
    state = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    pincode = models.IntegerField(
        "PIN code",
        help_text="6 digits [0-9] PIN code",
        validators=[MinValueValidator(100000), MaxValueValidator(999999)],
    )
    street_address = models.CharField(max_length=300,null=True,blank=True)
    house_choice = (("rent","rent"),("own house","own house"))
    house = models.CharField(max_length=15,choices=house_choice)
    is_allergies = models.BooleanField(default=False)
    is_fenced = models.BooleanField(default=False)
    why_do_you_want_a_dog = models.TextField()
    dog_be_confined_to_your_own_property = models.TextField()
    provide_exercise = models.TextField()
    training_willing_to_provide = models.TextField()
    correct_dog_if_misbehaves = models.TextField()
    takes_to_support_a_dog = models.TextField()
    choose_this_particular_dog = models.TextField()

    def __str__(self) -> str:
        return f" you have received inquiry from {self.user.first_name} " 







# @receiver(pre_save,sender = settings.AUTH_USER_MODEL)
# def pre_save_method(sender,instance,*args,**kwargs):
#     print(instance.email,instance.id)



@receiver(post_save,sender = AdoptionForm)
def show_instance(sender,instance,created,*args,**kwargs):
    dic = instance.__dict__
    name = instance
    if created == True:
        send_mail(
        'New Enquiry',
        str(instance),
        settings.EMAIL_HOST_USER,
        ['shashikantching@gmail.com',],
        fail_silently=False,)


        # print(f"created new object:sending mail to {instance.email}")
    # else:
    #     print(f"updated object:sending mail to {instance.email}")

# @receiver(post_delete,sender = settings.AUTH_USER_MODEL)
# def delete_instance(sender,instance,created,*args,**kwargs):
#     print(f"Deleted : {instance}")



