from django.db import models

from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel
)
from wagtail.snippets.models import register_snippet

from page.blocks import ImageGridBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock
from prayer_schedule.models import Prayer, PrayerScheduleExtra


@register_snippet
class Announcement(models.Model):
    title = models.CharField(max_length=80, help_text='80 characters maximum.')
    body = StreamField([
        ('description', RichTextBlock()),
    ], default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
    ]

    def __str__(self):
        return self.title


class BasePage(Page):
    class Meta:
        abstract = True


class StandardPage(BasePage):
    # Hero section of Page
    hero_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='2400X858px'
    )
    hero_heading = models.CharField(
        null=True,
        blank=True,
        max_length=140,
        help_text='40 character limit.'
        )
    hero_caption = models.CharField(
        null=True,
        blank=True,
        max_length=140,
        help_text='140 character limit.'
        )
    hero_cta = models.CharField(
        null=True,
        blank=True,
        verbose_name='Hero CTA',
        max_length=20,
        help_text='Text to display on Call to Action. 20 character limit.'
        )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text='Choose a page to link the Call to Action'
    )
    body = StreamField([
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ], default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_image'),
            FieldPanel('hero_heading', classname='full'),
            FieldPanel('hero_caption', classname='full'),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                FieldPanel('hero_cta_link'),
                ])
            ], heading='Hero Image'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['prayers'] = Prayer.objects.all().exclude(title='Duha').order_by('sorter')
        context['prayer_extra'] = PrayerScheduleExtra.objects.all()

        return context