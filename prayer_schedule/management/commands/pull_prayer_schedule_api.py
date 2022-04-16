from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.utils.timezone import get_current_timezone, make_aware
from datetime import datetime
from prayer_schedule.models import *

import requests, json
import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        print ("-------RUNNING PRAYER SCHEDULE API-------")
        p_api_setting = PrayerScheduleAPISetting.objects.get()
        url = 'http://www.islamicfinder.us/index.php/api/prayer_times?country=%s&zipcode=%s&latitude=%s&longitude=%s&timezone=%s&time_format=%s' % (p_api_setting.country, p_api_setting.zip_code, p_api_setting.latitude, p_api_setting.longitude, p_api_setting.time_zone, p_api_setting.time_format)
        counter = 0
        r = requests.get(url)
        j = json.loads(r.content)
        now = datetime.now()
        tz = get_current_timezone()

        prayers = j['results'].items()
        for key, value in prayers:
            prayer = now.strftime("%Y") +'-'+ now.strftime("%m") +'-'+ now.strftime("%d") +' '+ value
            aware = make_aware(datetime.strptime(prayer, "%Y-%m-%d %H:%M"))
            Prayer.objects.update_or_create(title = key, defaults={ 'sorter': counter, 'adhan': aware })
            counter += 1