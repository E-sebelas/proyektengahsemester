# Generated by Django 4.2.5 on 2023-10-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0003_auto_20231027_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Link',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Title',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
