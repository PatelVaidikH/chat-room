# Generated by Django 4.2 on 2023-06-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0052_alter_usermaster_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommaster',
            name='last_message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
