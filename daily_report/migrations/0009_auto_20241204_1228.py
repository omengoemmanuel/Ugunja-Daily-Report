# Generated by Django 3.2.24 on 2024-12-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0008_alter_main_trending_headline_trending_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_trending_headline',
            name='related_image_1',
            field=models.ImageField(blank=True, default='uploads/main_trending/main.jpg', null=True, upload_to='uploads/main_trending'),
        ),
        migrations.AddField(
            model_name='main_trending_headline',
            name='related_image_2',
            field=models.ImageField(blank=True, default='uploads/main_trending/main.jpg', null=True, upload_to='uploads/main_trending'),
        ),
        migrations.AddField(
            model_name='main_trending_headline',
            name='related_image_3',
            field=models.ImageField(blank=True, default='uploads/main_trending/main.jpg', null=True, upload_to='uploads/main_trending'),
        ),
    ]
