# Generated by Django 4.0.4 on 2022-05-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0003_rename_new_bio_player_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(through='raterprojectapi.Game_Category', to='raterprojectapi.category'),
        ),
    ]