# Generated by Django 4.0 on 2022-02-14 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0013_remove_adoptionform_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionform',
            name='send_form_to',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='adoption_form_to', to='pet_finder.animalshelter'),
            preserve_default=False,
        ),
    ]
