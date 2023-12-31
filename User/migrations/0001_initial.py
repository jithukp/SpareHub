# Generated by Django 3.1.1 on 2020-09-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(max_length=50, upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
