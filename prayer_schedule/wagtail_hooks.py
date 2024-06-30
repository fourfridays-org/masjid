from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel

from prayer_schedule.models import Prayer


class PrayerViewSet(SnippetViewSet):
    model = Prayer

    panels = [
        FieldPanel("sorter"),
        FieldPanel("title"),
        FieldPanel("adhan"),
        FieldPanel("salah"),
    ]

register_snippet(PrayerViewSet)
