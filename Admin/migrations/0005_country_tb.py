# Generated by Django 3.1.1 on 2020-10-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_model_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='country_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
            ],
        ),
    ]
