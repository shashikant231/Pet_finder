# Generated by Django 4.0 on 2022-02-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0022_rename_send_form_to_adoptionform_animal_shelter_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalshelter',
            name='adoption_procedure',
            field=models.TextField(blank=True, null=True),
        ),
    ]
