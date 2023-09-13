# Generated by Django 3.1.1 on 2020-10-13 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_district_tb'),
        ('Spare_Parts_Shop', '0008_tracking_details_tb_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop_tb',
            old_name='city',
            new_name='place',
        ),
        migrations.AddField(
            model_name='shop_tb',
            name='country_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Admin.country_tb'),
        ),
        migrations.AddField(
            model_name='shop_tb',
            name='district_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Admin.district_tb'),
        ),
        migrations.AddField(
            model_name='shop_tb',
            name='state_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Admin.state_tb'),
        ),
    ]