# Generated by Django 4.0.1 on 2022-08-11 10:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StripeSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(help_text='The start date of the subscription.')),
                ('status', models.CharField(help_text='The status of this subscription.', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, null=True, verbose_name='username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801865632882'. Up to 11 digits allowed.", regex='(^(\\+8801|8801|01|008801))[1|3-9]{1}(\\d){8}$'), django.core.validators.MaxLengthValidator(13), django.core.validators.MinLengthValidator(13)])),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Customer')])),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyStripeModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801865632882'. Up to 11 digits allowed.", regex='(^(\\+8801|8801|01|008801))[1|3-9]{1}(\\d){8}$'), django.core.validators.MaxLengthValidator(13), django.core.validators.MinLengthValidator(13)])),
                ('stripe_subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.stripesubscription')),
            ],
        ),
    ]
