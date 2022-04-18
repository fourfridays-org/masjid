# Generated by Django 4.0.2 on 2022-04-18 23:12

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='body',
            field=wagtail.core.fields.RichTextField(help_text='180 characters maximum.', max_length=180),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(help_text='80 characters maximum.', max_length=80),
        ),
    ]
