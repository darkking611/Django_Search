# Generated by Django 3.0.6 on 2020-05-23 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200519_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='search',
            new_name='new_search',
        ),
    ]
