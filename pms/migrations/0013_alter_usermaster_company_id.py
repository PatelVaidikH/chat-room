# Generated by Django 4.2 on 2023-05-30 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0012_alter_usermaster_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='company_id',
            field=models.IntegerField(null=True),
        ),
    ]
