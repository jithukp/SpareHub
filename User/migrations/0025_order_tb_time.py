# Generated by Django 3.1.1 on 2020-10-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0024_payment_tb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_tb',
            name='time',
            field=models.CharField(default='empty', max_length=20),
        ),
    ]