from django import forms

from wagtail.admin.panels import FieldPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import (
    BooleanBlock, CharBlock, ChoiceBlock, DateBlock, FieldBlock, PageChooserBlock, RawHTMLBlock, RichTextBlock, StreamBlock, StructBlock, URLBlock
)
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


class AlignmentBlock(ChoiceBlock):
    choices = [
        ('start', 'Left'),
        ('center', 'Center'),
        ('end', 'Right')
    ]


class AlignedRAWHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = AlignmentBlock(default='start')

    class Meta:
        template = 'blocks/aligned_raw_html_block.html'


class BackgroundColorBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), 
        ('white-smoke', 'White Smoke'),
        ('aqua-island', 'Aqua Island'),
        ('concrete', 'Concrete')
    ))


class BlockQuoteBlock(StructBlock):
    text = CharBlock(max_length=180, help_text='180 character limit.')
    cite = CharBlock(max_length=180, help_text='180 character limit.')

    class Meta:
        template = 'blocks/block_quote_block.html'


class ButtonBlock(StructBlock):
    alignment = AlignmentBlock(default='start')
    size = ChoiceBlock([
        ('sm', 'Small'),
        ('md', 'Medium'),
        ('lg', 'Large')
    ])
    cta_text = CharBlock(max_length=25, help_text='25 character limit.')
    internal_link = PageChooserBlock(required=False)
    external_link = URLBlock(required=False)
    color = ChoiceBlock([
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('dark-brown', 'Dark Brown'),
        ('white-smoke', 'White Smoke'),
        ('concrete', 'Concrete'),
        ('aqua-island', 'Aqua Island'),

    ])

    class Meta:
        icon = 'pick'
        template = 'blocks/button_block.html'


class DocumentBlock(StructBlock):
    document = DocumentChooserBlock(required=False)

    class Meta:
        icon = 'doc-full'
        template = 'blocks/document_block.html'


class PersonDateBlock(StructBlock):
    date = DateBlock(required=False)
    people = StreamBlock([
        ('person', SnippetChooserBlock('page.People')),
    ])

    panels = [
        # Use a FieldPanel because article.ArticleAuthor is registered as a snippet
        FieldPanel("people"),
    ]


class IconBlock(StructBlock):
    icon = ChoiceBlock([
        ('font-awesome', 'Font Awesome'),
    ])
    name = CharBlock(max_length=25, help_text='25 character limit')
    size = ChoiceBlock(choices = [
        ('xs', 'Extra Small'),
        ('sm', 'Small'),
        ('lg', 'Large'),
        ('xl', 'Extra Large'),
        ('2xl', 'Double XL')
    ])
    font_awesome_icon_choice = ChoiceBlock([
        ('solid', 'Solid'),
        ('regular', 'Regular'),
        ('light', 'Light'),
        ('brand', 'Brand')
    ], required=False)
    alignment = AlignmentBlock(default='start')

    class Meta:
        icon = 'wagtail'
        template = 'blocks/icon_block.html'


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)
    alignment = AlignmentBlock(default='start', required=False)
    border = BooleanBlock(required=False, help_text='Adds border around image')

    class Meta:
        icon = 'image'
        template = 'blocks/image_block.html'


class ImageGridBlock(StreamBlock):
    grid = StructBlock([
        ('image', ImageChooserBlock(required=True, help_text='size: 800X450px')),
        ('caption', CharBlock(max_length=26, help_text='26 characters limit')),
        ('description', CharBlock(max_length=300, required=False, help_text='300 characters limit')),
        ('link', PageChooserBlock(required=False))
    ])

    class Meta:
        icon = 'image'
        template = 'blocks/image_grid_block.html'


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h6 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6')
    ], blank=True, required=False)
    alignment = AlignmentBlock(default='start', required=False)

    class Meta:
        icon = 'pilcrow'
        template = 'blocks/heading_block.html'


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image', 'code', 'ol', 'strikethrough', 'superscript', 'subscript'],
        icon='pilcrow',
        template='blocks/paragraph_block.html'
    )
    image_block = ImageBlock()
    button_block = ButtonBlock()
    image_grid_block = ImageGridBlock()
    document_block = DocumentBlock()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='code',
        template='blocks/embed_block.html')
    icon_block = IconBlock()
    table = TableBlock(template='includes/table.html')
    block_quote = BlockQuoteBlock()
    raw_html = AlignedRAWHTMLBlock()


class SingleColumnBlock(StructBlock):
    column = BaseStreamBlock()
    alignment = AlignmentBlock(default='start', required=False)
    #background_color = BackgroundColorBlock(default='normal', required=False)

    class Meta:
        label = 'Single Column'
        template = 'blocks/single_column_block.html'


class TwoColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    alignment = AlignmentBlock(default='start', required=False)
    #background_color = BackgroundColorBlock(default='normal', required=False)

    class Meta:
        label = 'Two Columns'
        template = 'blocks/two_column_block.html'


class ThreeColumnBlock(StructBlock):
    left_column = BaseStreamBlock()
    middle_column = BaseStreamBlock()
    right_column = BaseStreamBlock()
    alignment = AlignmentBlock(default='start', required=False)
    #background_color = BackgroundColorBlock(default='normal', required=False)

    class Meta:
        label = 'Three Columns'
        template = 'blocks/three_column_block.html'


class FourColumnBlock(StructBlock):
    left_column_1 = BaseStreamBlock()
    left_column_2 = BaseStreamBlock()
    right_column_1 = BaseStreamBlock()
    right_column_2 = BaseStreamBlock()
    alignment = AlignmentBlock(default='start', requirement=False)
    #background_color = BackgroundColorBlock(default='normal', required=False)

    class Meta:
        label = 'Four Columns'
        template = 'blocks/four_column_block.html'