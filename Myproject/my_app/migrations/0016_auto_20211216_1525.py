# Generated by Django 3.2.9 on 2021-12-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0015_auto_20211216_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='email',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='s_member',
            name='email',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchman',
            name='email',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
