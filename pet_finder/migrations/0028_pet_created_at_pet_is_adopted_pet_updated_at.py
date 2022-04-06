# Generated by Django 4.0 on 2022-02-20 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0027_alter_pet_vaccination'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='is_adopted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
