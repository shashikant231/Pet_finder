# Generated by Django 4.0 on 2022-02-14 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0012_pet_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptionform',
            name='pincode',
        ),
    ]
