# Generated by Django 5.0 on 2023-12-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulreport', '0011_alter_report_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='admin_response',
            field=models.TextField(default=''),
        ),
    ]
