# Generated by Django 3.2.24 on 2025-01-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0052_lifestyle_col_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifestyle_col_4',
            name='type',
            field=models.CharField(default='Lifestyle', max_length=30),
        ),
    ]
