# Generated by Django 4.2 on 2023-05-30 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0022_alter_roommaster_chat_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetail',
            name='chat_room_id',
            field=models.IntegerField(),
        ),
    ]
