# Generated by Django 3.2.5 on 2021-09-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_img',
            field=models.ImageField(default='user-01.png', unique=True, upload_to='userImg/', verbose_name='accountImg'),
        ),
    ]
