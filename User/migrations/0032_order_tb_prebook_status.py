# Generated by Django 3.1.1 on 2021-04-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0031_auto_20210329_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_tb',
            name='prebook_status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
