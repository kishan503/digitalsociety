# Generated by Django 3.2.9 on 2021-12-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0018_visitor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='d_t',
            new_name='date',
        ),
        migrations.AddField(
            model_name='visitor',
            name='time',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
