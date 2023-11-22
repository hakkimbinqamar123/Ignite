from django.contrib import admin
from .models import *
from django.utils.html import format_html


class JudgeAdmin(admin.ModelAdmin):
    list_display = ('j_id', 'username', 'email', 'phone', 'qualification', 'event')
    list_filter = ('event',)
    ordering = ('event__pgm_name',)

    def event(self, obj):
        if obj.event:
            return obj.event.pgm_name
        else:
            return '-'

admin.site.register(Judge, JudgeAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'pgm_name', 'venue_name', 'start_time', 'end_time', 'display_image', 'about', 'description', 'heading', 'rate', 'status')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        else:
            return ''

    display_image.short_description = 'Image Preview'

admin.site.register(Event, EventAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('event', 'candidate_id', 'position', 'grade', 'judge')
    ordering = ('event_id__pgm_name',)

    def event(self, obj):
        return format_html('<span style="color: #3366cc;">{}</span>', obj.event_id.pgm_name)

    def judge(self, obj):
        return format_html('<span style="color: #cc3366;">{}</span>', obj.j_id.username)

admin.site.register(Result, ResultAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('candidate_id', 'username', 'display_image', 'college','phone')  # Add 'display_image' to list_display

    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.id_card.url)

    display_image.short_description = 'ID Card'  # Set the column header name

admin.site.register(Student, StudentAdmin)

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
admin.site.register(Venue, VenueAdmin)

