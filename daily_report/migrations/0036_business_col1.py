# Generated by Django 3.2.24 on 2024-12-19 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0035_comment_cul_col3'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_col1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='culture', max_length=30)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=300)),
                ('writer_name', models.CharField(max_length=30)),
                ('photo', models.ImageField(default='uploads/culture/culture.jpg', upload_to='uploads/culture')),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
