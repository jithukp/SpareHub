# Generated by Django 3.1.1 on 2020-10-08 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Workshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=20)),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Workshop.workshop_tb')),
            ],
        ),
    ]
