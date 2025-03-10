from django.contrib import admin
from .models import About, ContactMeForm
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(ContactMeForm)
class ContactMeFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email')
    list_filter = ('created_on',)
