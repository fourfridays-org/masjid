from django.db import models

from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from page.models import BasePage

class EventIndexPage(BasePage):
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

    subpage_types = ['EventPage']

    content_panels = BasePage.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_image'),
            FieldPanel('hero_heading', classname='full'),
            FieldPanel('hero_caption', classname='full'),
            ], heading='Hero Image'),
    ]

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        context['events'] = EventPage.objects.live().all()

        return context


class EventPage(BasePage):
    hero_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='2400X858px'
    )
    body = StreamField([
        ('description', RichTextBlock()),
    ], default='')
    start_time = models.DateTimeField(default='2022-04-21 00:00')
    end_time = models.DateTimeField(default='2022-04-21 00:00')

    # Empty list means that no child content types are allowed.
    subpage_types = []

    content_panels = BasePage.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('body'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
    ]
