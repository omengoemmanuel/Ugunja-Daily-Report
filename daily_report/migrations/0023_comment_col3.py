# Generated by Django 3.2.24 on 2024-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0022_sub_trending_col_3_trend_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_col3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('image', models.ImageField(default='uploads/comments/default.jpg', upload_to='uploads/comments')),
            ],
        ),
    ]