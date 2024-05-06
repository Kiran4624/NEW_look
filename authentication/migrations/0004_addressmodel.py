# Generated by Django 5.0.4 on 2024-04-20 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_registermodel_is_activate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]