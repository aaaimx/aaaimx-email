from django.contrib import admin
from .models import Email, Template
from emails.tasks import send_email
from django.db.models import F
from .utils import parse_template
# Register your models here.

@admin.register(Template)
class AdminTemplate(admin.ModelAdmin):
    list_display = ('name', 'file_name', 'keys')
    list_filter = ('name',)

@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'message', 'template', 'recipients', 'sent')
    list_filter = ('subject', 'message', 'recipients', 'template', 'sent' )
    search_fields = ('message', 'recipients')
    actions = ['send_email_from_contact',]

    def send_email_from_contact(self, request, queryset):
        queryset.update(sent=F('sent') + 1)
        for q in queryset:
            template = parse_template(q.context, q.template)
            send_email(q.subject, q.message, q.recipients, template)
    send_email_from_contact.short_description = "Send selected emails"