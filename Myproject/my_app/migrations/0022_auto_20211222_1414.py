# Generated by Django 3.2.9 on 2021-12-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0021_auto_20211222_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]