# Generated by Django 4.2.1 on 2023-07-29 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_name_menu_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='title',
            new_name='name',
        ),
    ]