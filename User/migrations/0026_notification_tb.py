# Generated by Django 3.1.1 on 2020-12-12 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spare_Parts_Shop', '0012_spare_part_tb_category_id'),
        ('User', '0025_order_tb_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(max_length=20)),
                ('record_id', models.IntegerField()),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spare_Parts_Shop.shop_tb')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_tb')),
            ],
        ),
    ]
