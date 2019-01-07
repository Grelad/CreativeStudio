from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'email']

    class Meta:
        model: Subscriber


admin.site.register(Subscriber, SubscriberAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Schedule._meta.fields]
    list_filter = ['title']
    search_fields = ['title', 'content']

    class Meta:
        model: Schedule


admin.site.register(Schedule, ScheduleAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About._meta.fields]
    list_filter = ['title']
    search_fields = ['title', 'content']

    class Meta:
        model: About


admin.site.register(About, AboutAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]
    list_filter = ['title']
    search_fields = ['title', 'content']

    class Meta:
        model: Contact


admin.site.register(Contact, ContactAdmin)
