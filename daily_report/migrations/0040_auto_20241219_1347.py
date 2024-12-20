# Generated by Django 3.2.24 on 2024-12-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0039_business_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_main_support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supporting_photo', models.ImageField(default='uploads/business/business.jpg', upload_to='uploads/business')),
                ('supporting_photo_title', models.CharField(default='', max_length=300)),
                ('supporting_photo_description', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='business_col1',
            name='photo',
            field=models.ImageField(default='uploads/business/business.jpg', upload_to='uploads/business'),
        ),
        migrations.AlterField(
            model_name='business_main',
            name='photo',
            field=models.ImageField(default='uploads/business/business.jpg', upload_to='uploads/business'),
        ),
    ]
