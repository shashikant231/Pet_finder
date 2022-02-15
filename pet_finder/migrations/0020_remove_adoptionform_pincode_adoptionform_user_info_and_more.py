# Generated by Django 4.0 on 2022-02-15 09:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0019_adoptionform_created_at_adoptionform_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptionform',
            name='pincode',
        ),
        migrations.AddField(
            model_name='adoptionform',
            name='user_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='adoption_form_user_info', to='pet_finder.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('profile_pic', models.ImageField(blank=True, upload_to='media/')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='For e.g +91-95544-95544, +91-12345-54321, etc.', max_length=128, region=None, verbose_name='Phone Number')),
                ('pincode', models.IntegerField(help_text='6 digits [0-9] PIN code', validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)], verbose_name='PIN code')),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=80)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pet_finder.user')),
            ],
        ),
    ]