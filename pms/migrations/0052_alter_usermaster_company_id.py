# Generated by Django 4.2 on 2023-06-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0051_usermaster_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='company_id',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
