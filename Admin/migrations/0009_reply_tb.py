# Generated by Django 3.1.1 on 2021-01-01 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0030_auto_20201213_1843'),
        ('Admin', '0008_part_category_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=20)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.complaint_tb')),
            ],
        ),
    ]
