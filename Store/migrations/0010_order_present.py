# Generated by Django 3.1.5 on 2021-01-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
