# Generated by Django 3.2.24 on 2024-12-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0017_alter_sub_trending_col_3_writter'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_trending_col_1',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sub_trending_col_2',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sub_trending_col_3',
            name='description',
            field=models.TextField(default=''),
        ),
    ]