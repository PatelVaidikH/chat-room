# Generated by Django 4.2 on 2023-05-31 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0034_alter_roommaster_date_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetail',
            name='timestamp',
        ),
    ]
