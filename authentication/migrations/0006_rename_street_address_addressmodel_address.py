# Generated by Django 5.0.4 on 2024-04-23 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_rename_customer_id_addressmodel_c_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addressmodel',
            old_name='street_address',
            new_name='address',
        ),
    ]
