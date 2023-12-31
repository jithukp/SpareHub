# Generated by Django 3.1.1 on 2020-09-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spare_Parts_Shop', '0006_spare_part_tb_shop_id'),
        ('User', '0002_auto_20200921_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('total_price', models.CharField(max_length=20)),
                ('part_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spare_Parts_Shop.spare_part_tb')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_tb')),
            ],
        ),
    ]
