# Generated by Django 3.1.1 on 2020-09-30 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spare_Parts_Shop', '0006_spare_part_tb_shop_id'),
        ('User', '0012_auto_20200930_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_tb',
            name='shop_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Spare_Parts_Shop.shop_tb'),
        ),
    ]
