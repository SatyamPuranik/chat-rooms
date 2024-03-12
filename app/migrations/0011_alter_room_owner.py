# Generated by Django 4.1.4 on 2024-02-12 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_room_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
