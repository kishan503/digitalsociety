# Generated by Django 3.2.9 on 2021-12-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0016_auto_20211216_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='flat_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='s_member',
            name='flat_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
