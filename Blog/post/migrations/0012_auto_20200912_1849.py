# Generated by Django 3.1.1 on 2020-09-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
