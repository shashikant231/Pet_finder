# Generated by Django 4.0 on 2022-01-30 12:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0004_animalshelter_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalshelter',
            name='contact_no',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='For e.g +91-95544-95544, +91-12345-54321, etc.', max_length=128, region=None, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pet',
            name='size',
            field=models.CharField(choices=[('Puppy', 'Puppy'), ('Adult', 'Adult'), ('Medium', 'Medium')], max_length=10),
        ),
    ]