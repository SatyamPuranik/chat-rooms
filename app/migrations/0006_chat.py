# Generated by Django 4.1.4 on 2024-02-12 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_room_room_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=255)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
    ]