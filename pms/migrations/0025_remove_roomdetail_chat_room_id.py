# Generated by Django 4.2 on 2023-05-30 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0024_alter_roomdetail_chat_room_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetail',
            name='chat_room_id',
        ),
    ]
