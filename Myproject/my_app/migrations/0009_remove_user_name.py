# Generated by Django 3.2.9 on 2021-12-14 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
