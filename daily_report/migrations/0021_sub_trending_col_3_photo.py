# Generated by Django 3.2.24 on 2024-12-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0020_comment_col2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_trending_col_3',
            name='photo',
            field=models.ImageField(default='uploads/sub trending col 3/sub.jpg', upload_to='uploads/sub trending col 3'),
        ),
    ]
