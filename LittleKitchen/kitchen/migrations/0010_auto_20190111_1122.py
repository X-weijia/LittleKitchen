# Generated by Django 2.1.3 on 2019-01-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0009_guanzhu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.TextField(verbose_name='手机号'),
        ),
    ]
