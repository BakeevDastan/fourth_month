# Generated by Django 4.1.1 on 2022-09-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_genre_alter_review_options_alter_review_film_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'жанр', 'verbose_name_plural': 'жанры'},
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]