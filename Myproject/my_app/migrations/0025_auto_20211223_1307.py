# Generated by Django 3.2.9 on 2021-12-23 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0024_rename_complain_complaint'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='complaint',
            new_name='comp_details',
        ),
        migrations.RenameModel(
            old_name='suggestion',
            new_name='sugg_details',
        ),
    ]