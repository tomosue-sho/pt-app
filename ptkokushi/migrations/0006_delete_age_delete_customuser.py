# Generated by Django 4.2.7 on 2023-12-18 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptkokushi', '0005_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Age',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
