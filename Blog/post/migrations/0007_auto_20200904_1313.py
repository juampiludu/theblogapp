# Generated by Django 3.1.1 on 2020-09-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200904_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='preview_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
