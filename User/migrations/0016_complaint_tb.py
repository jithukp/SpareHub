# Generated by Django 3.1.1 on 2020-10-05 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_auto_20201005_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('complaint', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_tb')),
            ],
        ),
    ]
