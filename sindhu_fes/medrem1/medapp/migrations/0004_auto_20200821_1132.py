# Generated by Django 3.1 on 2020-08-21 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0003_meddata_mrg_med'),
    ]

    operations = [
        migrations.AddField(
            model_name='meddata',
            name='evng_med',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meddata',
            name='noon_med',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
