# Generated by Django 4.0.3 on 2022-03-26 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_bird_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bird',
            old_name='Birdhouse',
            new_name='Birdhouses',
        ),
    ]
