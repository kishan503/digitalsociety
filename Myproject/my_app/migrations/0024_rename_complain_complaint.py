# Generated by Django 3.2.9 on 2021-12-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0023_complain_suggestion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='complain',
            new_name='complaint',
        ),
    ]