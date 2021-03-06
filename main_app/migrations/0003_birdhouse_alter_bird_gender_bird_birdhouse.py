# Generated by Django 4.0.3 on 2022-03-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_bird_user_alter_bird_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirdHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='bird',
            name='gender',
            field=models.CharField(choices=[('f', 'female'), ('m', 'male')], max_length=10),
        ),
        migrations.AddField(
            model_name='bird',
            name='Birdhouse',
            field=models.ManyToManyField(to='main_app.birdhouse'),
        ),
    ]
