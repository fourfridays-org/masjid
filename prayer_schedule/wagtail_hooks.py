from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from prayer_schedule.models import *


class PrayerModelAdmin(ModelAdmin):
    model = Prayer
    menu_icon = 'date'  # change as required
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_per_page = 50
    list_display = ('title', 'adhan', 'salah')
    #ordering = ['title']
    #list_filter = ('offering_id', 'offering_code')
    search_fields = ('title')

modeladmin_register(PrayerModelAdmin)