from django.contrib import admin

from .models import URLModel


@admin.register(URLModel)
class URLAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_url', 'modified_url') 