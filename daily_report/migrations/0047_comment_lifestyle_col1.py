# Generated by Django 3.2.24 on 2025-01-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0046_lifestyle_col1'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_lifestyle_col1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm', models.TextField()),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('image', models.ImageField(default='uploads/comments/default.jpg', upload_to='uploads/comments')),
            ],
        ),
    ]
