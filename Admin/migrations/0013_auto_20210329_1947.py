# Generated by Django 3.1.1 on 2021-03-29 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0012_remove_district_tb_state_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state_tb',
            name='country_id',
        ),
        migrations.DeleteModel(
            name='country_tb',
        ),
        migrations.DeleteModel(
            name='state_tb',
        ),
    ]
