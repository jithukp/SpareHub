# Generated by Django 3.1.1 on 2021-01-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_reply_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply_tb',
            name='status',
            field=models.CharField(default='unread', max_length=20),
        ),
    ]
