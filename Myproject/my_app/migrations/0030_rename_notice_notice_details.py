# Generated by Django 3.2.9 on 2021-12-28 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0029_notice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='notice',
            new_name='notice_details',
        ),
    ]
