# Generated by Django 3.2.9 on 2021-12-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0026_auto_20211224_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]