# Generated by Django 5.0.4 on 2024-04-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('resolved', 'Resolved'), ('unresolved', 'Unresolved'), ('on_working', 'On Working')], default='unresolved', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
