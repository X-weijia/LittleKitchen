# Generated by Django 2.1.3 on 2019-01-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_auto_20190109_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='season',
            field=models.CharField(default='', max_length=11, verbose_name='季节'),
        ),
    ]