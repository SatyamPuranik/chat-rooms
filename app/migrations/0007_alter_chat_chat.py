# Generated by Django 4.1.4 on 2024-02-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
