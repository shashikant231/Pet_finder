# Generated by Django 4.0 on 2022-02-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0024_adoptionform_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionform',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
