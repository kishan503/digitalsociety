# Generated by Django 3.2.9 on 2021-12-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='dob',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
