# Generated by Django 4.0 on 2022-01-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0009_merge_20220130_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
