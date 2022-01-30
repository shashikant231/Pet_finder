# Generated by Django 4.0 on 2022-01-29 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0005_pet_is_rescued_pet_story_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalshelter',
            old_name='name',
            new_name='organisations_name',
        ),
        migrations.RemoveField(
            model_name='animalshelter',
            name='email',
        ),
        migrations.AddField(
            model_name='animalshelter',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animalshelter',
            name='organisations_mission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animalshelter',
            name='organisations_policies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animalshelter',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]