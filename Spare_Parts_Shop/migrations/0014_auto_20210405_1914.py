# Generated by Django 3.1.1 on 2021-04-05 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_auto_20210329_1947'),
        ('Spare_Parts_Shop', '0013_auto_20210329_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spare_part_tb',
            name='model_id',
        ),
        migrations.CreateModel(
            name='part_model_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.model_tb')),
                ('part_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spare_Parts_Shop.spare_part_tb')),
            ],
        ),
    ]
