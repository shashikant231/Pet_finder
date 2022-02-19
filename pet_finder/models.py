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

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to ='media/', blank=True)
    phone_number = PhoneNumberField("Phone Number", help_text=PHONE_HELP_TEXT)
    pincode = models.IntegerField(
        "PIN code",
        help_text="6 digits [0-9] PIN code",
        validators=[MinValueValidator(100000), MaxValueValidator(999999)],
    )
    state = models.CharField(max_length=50,null=False)
    city = models.CharField(max_length=80,null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class AnimalShelter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="animal_name")
    profile_pic = models.ImageField(upload_to ='media/')
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
    adoption_procedure = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.organisations_name



class Pet(models.Model):
    name = models.CharField(max_length=100,blank=False)
    breed = models.CharField(max_length=30,blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    gender = models.CharField(choices=gender_choices, max_length=10)
    color = models.CharField(max_length=50,blank=True)
    age = models.CharField(max_length=30,blank=False)
    size_choices = (("Puppy", "Puppy"), ("Adult", "Adult"),("Medium","Medium"))
    size = models.CharField(choices=size_choices,max_length=10,blank=False)
    vaccination_choices = (("Not Vaccianted", "Not Vaccianted"), 
                            ("Partially Vaccinated", "Partially Vaccinated"),
                            ("Completely Vaccinated","Completely Vaccinated"))
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
    user_id  = models.ForeignKey(User,on_delete=models.CASCADE,related_name="adoption_form_user")
    user_info_id = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name="adoption_form_user_info")
    animal_shelter_id = models.ForeignKey(AnimalShelter,on_delete=models.CASCADE,related_name="adoption_form_to")
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE,related_name='adoption_form_pet')
    state = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
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
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    status_choice = (('Pending','Pending'),('Accepted','Accepted'),('Rejected','Rejected'))
    status = models.CharField(choices=status_choice,max_length=20,default='pending')

    def __str__(self) -> str:
        return f" you have received inquiry from {self.user_id.first_name} " 




@receiver(post_save,sender = AdoptionForm)
def show_instance(sender,instance,created,*args,**kwargs):
    dic = instance.__dict__
    from .serializers import AdoptionFormSerializer

    data = AdoptionFormSerializer(instance).data
    print((data))
    state = data['state']
    city = data['city']
    street_address = data['street_address']
    house = data['house']
    house = data['house']
    is_fenced = data['is_fenced']
    why_do_you_want_a_dog = data['why_do_you_want_a_dog']
    dog_be_confined_to_your_own_property = data['dog_be_confined_to_your_own_property']
    provide_exercise = data['provide_exercise']
    training_willing_to_provide = data['training_willing_to_provide']
    correct_dog_if_misbehaves = data['correct_dog_if_misbehaves']
    takes_to_support_a_dog = data['takes_to_support_a_dog']
    choose_this_particular_dog = data['choose_this_particular_dog']
    pet_image = data['pet_image']
    user_pincode = data['user_pincode']
    user_state = data['user_state']
    user_city = data['user_city']




    if created == True:
        send_mail(
        'New Enquiry',
        f"{user_pincode},{user_city},{user_city},{house},{why_do_you_want_a_dog},{pet_image},{dog_be_confined_to_your_own_property},{provide_exercise},{training_willing_to_provide},{correct_dog_if_misbehaves},{takes_to_support_a_dog},{choose_this_particular_dog},{house},{is_fenced},{state},{city},{street_address}",
        settings.EMAIL_HOST_USER,
        ['shashikantching@gmail.com',],
        fail_silently=False,)

    if created == False:
        if instance.status == "Accepted":
            animal_shelter_id = instance.animal_shelter_id.id
            user_id = instance.user_id.id
            organistion_name = AnimalShelter.objects.filter(id=animal_shelter_id).values('organisations_name')[0]['organisations_name']
            user_email = User.objects.filter(id=user_id).values('email')[0]['email']
            send_mail(
                'Enquiry Accepted',
                f"{organistion_name} has accepted has accepted your adoption form and would like to proceed with the adoption process. Please keep a check on your emails and messages, you will be contacted by the {organistion_name} shortly.",
                settings.EMAIL_HOST_USER,
                [user_email,],
        fail_silently=False,

            )
        elif instance.status == "Rejected":
            animal_shelter_id = instance.animal_shelter_id.id
            user_id = instance.user_id.id
            organistion_name = AnimalShelter.objects.filter(id=animal_shelter_id).values('organisations_name')[0]['organisations_name']
            user_email = User.objects.filter(id=user_id).values('email')[0]['email']
            send_mail(
                'Enquiry Rejected',
                f"We are sorry to inform you that the {organistion_name} cannot move forward with your adoption application. Try applying for other pets.Thanks",
                settings.EMAIL_HOST_USER,
                [user_email,],
        fail_silently=False,

            )





