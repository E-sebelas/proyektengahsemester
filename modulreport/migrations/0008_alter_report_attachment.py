# Generated by Django 4.2.6 on 2023-10-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulreport', '0007_report_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
