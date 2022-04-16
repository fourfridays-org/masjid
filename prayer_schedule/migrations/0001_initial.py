# Generated by Django 4.0.2 on 2022-04-15 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorter', models.CharField(blank=True, default='', max_length=1, null=True)),
                ('title', models.CharField(max_length=7, unique=True)),
                ('azan', models.DateTimeField(blank=True, null=True)),
                ('salah', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
