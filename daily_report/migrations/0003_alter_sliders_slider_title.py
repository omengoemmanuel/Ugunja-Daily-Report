# Generated by Django 3.2.24 on 2024-12-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0002_alter_sliders_slider_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliders',
            name='slider_title',
            field=models.CharField(max_length=200),
        ),
    ]