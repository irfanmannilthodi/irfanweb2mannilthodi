# Generated by Django 4.2.10 on 2024-03-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0002_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hello', upload_to='pics'),
            preserve_default=False,
        ),
    ]
