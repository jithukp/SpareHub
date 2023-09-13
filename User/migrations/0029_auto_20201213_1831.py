# Generated by Django 3.1.1 on 2020-12-13 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0028_auto_20201213_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification_tb',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.order_tb'),
        ),
        migrations.AlterField(
            model_name='notification_tb',
            name='prebook_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.prebook_tb'),
        ),
    ]