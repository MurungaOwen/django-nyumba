# Generated by Django 4.2.5 on 2023-11-03 19:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0004_rename_is_tenant_customuser_is_houseagent'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='agent')),
            ],
        ),
    ]