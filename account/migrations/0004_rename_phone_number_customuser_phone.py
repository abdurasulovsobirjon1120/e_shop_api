# Generated by Django 5.0.6 on 2024-06-11 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customuser_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
