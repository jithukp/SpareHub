# Generated by Django 3.1.1 on 2020-10-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_rating_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_tb',
            name='rating',
            field=models.CharField(max_length=20),
        ),
    ]
