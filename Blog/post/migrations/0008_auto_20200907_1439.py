# Generated by Django 3.1.1 on 2020-09-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200904_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
