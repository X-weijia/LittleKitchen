# Generated by Django 2.1.3 on 2019-01-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0006_auto_20190110_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='值')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
            ],
            options={
                'verbose_name_plural': '菜谱分类表',
            },
        ),
    ]
