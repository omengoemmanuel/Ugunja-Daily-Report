# Generated by Django 3.2.24 on 2024-12-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0009_auto_20241204_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]