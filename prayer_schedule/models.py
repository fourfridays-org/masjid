from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, RichTextField
from wagtail.snippets.models import register_snippet


@register_snippet
class PrayerScheduleAPISetting(models.Model):
    zip_code = models.CharField(max_length=5)
    country = models.CharField(max_length=2, help_text="Two letter abbreviation for county. Country Code. Ex: US, MX, ES, etc.")
    latitude = models.FloatField()
    longitude = models.FloatField()
    time_format = models.IntegerField(default=0, help_text="0: 24hr; 1: 12hr; 2: 12hr without suffix; 3: floating")
    time_zone = models.CharField(max_length=120)

    panels = [
        FieldPanel('zip_code'),
        FieldPanel('country'),
        FieldPanel('latitude'),
        FieldPanel('longitude'),
        FieldPanel('time_format'),
        FieldPanel('time_zone')
    ]

    def __str__(self):
        return self.zip_code


@register_snippet
class PrayerScheduleExtra(models.Model):
    title = models.CharField(max_length=120, help_text='120 max characters', default='')
    text = RichTextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.title


class Prayer(models.Model):
    sorter = models.CharField(max_length=1, null=True, blank=True, default='')
    title = models.CharField(max_length=7, unique=True)
    adhan = models.DateTimeField(null=True, blank=True, help_text="Any changes to adhan time will be overwritten by the API")
    salah = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.title