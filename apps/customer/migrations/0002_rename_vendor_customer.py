# Generated by Django 4.0.3 on 2022-07-04 11:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendor',
            new_name='Customer',
        ),
    ]