# Generated by Django 3.1.1 on 2020-09-12 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20200912_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]
