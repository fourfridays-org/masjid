# Generated by Django 4.0.2 on 2022-04-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_alter_eventpage_end_time_alter_eventpage_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='end_time',
            field=models.DateTimeField(default='2022, 4, 21'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='start_time',
            field=models.DateTimeField(default='2022, 4, 21'),
        ),
    ]
