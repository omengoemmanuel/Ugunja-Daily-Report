# Generated by Django 3.2.24 on 2024-12-04 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='fname',
            new_name='full_name',
        ),
    ]
