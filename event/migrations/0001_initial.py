# Generated by Django 5.0.6 on 2024-06-30 01:37

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_heading', models.CharField(blank=True, help_text='40 character limit.', max_length=140, null=True)),
                ('hero_caption', models.CharField(blank=True, help_text='140 character limit.', max_length=140, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('description', wagtail.blocks.RichTextBlock())], default='')),
                ('start_time', models.DateTimeField(default='2022-04-21 00:00')),
                ('end_time', models.DateTimeField(default='2022-04-21 00:00')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
