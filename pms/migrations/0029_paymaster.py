# Generated by Django 4.2 on 2023-05-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0028_roomdetail_chat_room_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_room_id', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('transaction_id', models.CharField(max_length=99)),
                ('sender_user_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('mode_of_payment', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'payment_sheet',
            },
        ),
    ]
