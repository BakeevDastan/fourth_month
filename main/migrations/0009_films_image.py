# Generated by Django 4.1.1 on 2022-09-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_films_genre_films_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='image',
            field=models.ImageField(null=True, upload_to='films'),
        ),
    ]
