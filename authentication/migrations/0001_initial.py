# Generated by Django 5.0.4 on 2024-04-17 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registerModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('c_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('otp', models.CharField(default='111111', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
      
    ]
