# Generated by Django 3.2.5 on 2021-09-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210926_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_img',
            field=models.FileField(default='user-01.png', unique=True, upload_to='', verbose_name='accountImg'),
        ),
    ]