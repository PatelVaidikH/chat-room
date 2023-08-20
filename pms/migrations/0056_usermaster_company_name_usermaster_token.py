# Generated by Django 4.2 on 2023-06-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0055_remove_usermaster_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='company_name',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='usermaster',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]