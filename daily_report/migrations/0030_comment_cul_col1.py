# Generated by Django 3.2.24 on 2024-12-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0029_remove_culture_col12_brief_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_cul_col1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm', models.TextField()),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
