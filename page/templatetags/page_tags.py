from django import template
from django.utils import timezone
from page.models import Announcement

import datetime

register = template.Library()


# ===============================================
# =            ANNOUNCEMENT TAG                 =
# ===============================================
@register.inclusion_tag('tags/announcement.html', takes_context=True)
def announcement(context):
    announcements = Announcement.objects.filter(end_date__gte=timezone.make_aware(datetime.datetime.now())).order_by('start_date')[:1]
    context['announcements'] = announcements
    
    return context