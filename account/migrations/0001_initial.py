# Generated by Django 3.1.5 on 2021-01-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=18)),
                ('address', models.TextField(max_length=500)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
