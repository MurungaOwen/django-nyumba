# Generated by Django 4.2.5 on 2023-10-31 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_merge_20231020_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_tenant',
            new_name='is_houseAgent',
        ),
    ]