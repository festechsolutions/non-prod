# Generated by Django 3.1 on 2020-08-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0004_auto_20200821_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meddata',
            name='evng_med',
            field=models.TimeField(default='PM'),
        ),
    ]
