# Generated by Django 3.1.5 on 2021-01-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0005_auto_20210115_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='participants',
            new_name='no_of_people',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='rtype',
            new_name='participation_type',
        ),
    ]
