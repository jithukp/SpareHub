# Generated by Django 3.1.1 on 2020-10-04 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spare_Parts_Shop', '0008_tracking_details_tb_time'),
        ('User', '0013_payment_tb_shop_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=200)),
                ('part_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spare_Parts_Shop.spare_part_tb')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user_tb')),
            ],
        ),
    ]
