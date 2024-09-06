from django.contrib import admin
from .models import Resource, Report, UserProfile, Activity, Notification

admin.site.register(Report)
admin.site.register(Resource)
admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Notification)