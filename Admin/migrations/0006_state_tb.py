# Generated by Django 3.1.1 on 2020-10-13 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_country_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.country_tb')),
            ],
        ),
    ]
