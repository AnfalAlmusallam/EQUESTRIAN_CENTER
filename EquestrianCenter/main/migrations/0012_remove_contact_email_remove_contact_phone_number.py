# Generated by Django 4.1.5 on 2023-02-25 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
    ]
