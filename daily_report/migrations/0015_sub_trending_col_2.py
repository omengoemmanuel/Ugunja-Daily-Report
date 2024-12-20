# Generated by Django 3.2.24 on 2024-12-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0014_alter_sub_trending_col_1_trending_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_trending_col_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trending_photo', models.ImageField(default='uploads/sub trending col 2/sub.jpg', upload_to='uploads/sub trending col 2')),
                ('trending_type', models.CharField(choices=[('Food', 'Food'), ('Sport', 'Sport'), ('Design', 'Design'), ('Business', 'Business'), ('Tech', 'Tech'), ('Travel', 'Travel')], max_length=30)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=300)),
            ],
        ),
    ]
