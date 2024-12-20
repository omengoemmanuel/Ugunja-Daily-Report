# Generated by Django 3.2.24 on 2024-12-19 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0041_business_sub_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_post_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='uploads/business/business.jpg', upload_to='uploads/business')),
                ('type', models.CharField(default='business', max_length=30)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=300)),
                ('brief_description', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('writer_name', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
