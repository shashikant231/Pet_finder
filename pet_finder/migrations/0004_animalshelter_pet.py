# Generated by Django 4.0 on 2022-01-16 18:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0003_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalShelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(help_text='For e.g +91-95544-95544, +91 12345-54321, etc.', max_length=128, region=None, verbose_name='Phone Number')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('pincode', models.IntegerField(help_text='6 digits [0-9] PIN code', validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)], verbose_name='PIN code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='animal_name', to='pet_finder.user')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('P', 'Puppy'), ('A', 'Adult'), ('M', 'Medium')], max_length=1)),
                ('vaccination', models.BooleanField(default='false')),
                ('first_image', models.ImageField(upload_to='media/')),
                ('second_image', models.ImageField(upload_to='media/')),
                ('adoption_fee', models.PositiveIntegerField(blank=True)),
                ('animal_shelter', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='pet_shelter', to='pet_finder.animalshelter')),
            ],
        ),
    ]
