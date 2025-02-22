# Generated by Django 3.2.24 on 2024-12-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0025_auto_20241214_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='culture_main_support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supporting_photo', models.ImageField(default='uploads/culture/culture.jpg', upload_to='uploads/culture')),
                ('supporting_photo_title', models.CharField(default='', max_length=300)),
                ('supporting_photo_description', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='culture_main',
            name='supporting_photo',
        ),
        migrations.RemoveField(
            model_name='culture_main',
            name='supporting_photo_description',
        ),
        migrations.RemoveField(
            model_name='culture_main',
            name='supporting_photo_title',
        ),
    ]
