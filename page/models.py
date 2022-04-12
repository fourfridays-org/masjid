from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
)

from .blocks import ImageGridBlock, SingleColumnBlock, TwoColumnBlock, ThreeColumnBlock, FourColumnBlock, HeroImageBlock


class BasePage(Page):
    class Meta:
        abstract = True


class StandardPage(BasePage):
    body = StreamField([
        ('hero_image', HeroImageBlock(icon='image')),
        ('single_column', SingleColumnBlock(group='COLUMNS')),
        ('two_columns', TwoColumnBlock(group='COLUMNS')),
        ('three_columns', ThreeColumnBlock(group='COLUMNS')),
        ('four_columns', FourColumnBlock(group='COLUMNS')),
        ('image_grid', ImageGridBlock(icon='image', min_num=2, max_num=4, help_text='Minimum 2 blocks and a maximum of 4 blocks')),
    ],default='')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]