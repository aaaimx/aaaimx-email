from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'message', 'html_message', 'recipients')
    list_filter = ('subject', 'message', 'html_message', 'recipients' )