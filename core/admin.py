from django.contrib import admin
from .models import Event, Media, Update, PrayerRequest

admin.site.register(Event)
admin.site.register(Media)
admin.site.register(Update)
admin.site.register(PrayerRequest)
