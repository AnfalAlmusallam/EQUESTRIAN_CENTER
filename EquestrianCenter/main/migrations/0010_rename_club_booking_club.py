# Generated by Django 4.1.5 on 2023-02-23 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Club',
            new_name='club',
        ),
    ]
