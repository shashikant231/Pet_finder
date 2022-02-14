# Generated by Django 4.0 on 2022-02-08 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0011_adoptionform'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pincode',
            field=models.IntegerField(default=123456, help_text='6 digits [0-9] PIN code', validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)], verbose_name='PIN code'),
            preserve_default=False,
        ),
    ]