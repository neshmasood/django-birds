# Generated by Django 4.0.3 on 2022-03-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_birdhouse_alter_bird_gender_bird_birdhouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=10),
        ),
    ]
