from django.contrib import admin
from .models import Email, Template
from emails.tasks import send_email
from django.db.models import F
from .utils import parse_template
# Register your models here.

@admin.register(Template)
class AdminTemplate(admin.ModelAdmin):
    list_display_links = ('pk', 'name',)
    list_display = ('pk', 'name', 'file', 'context')
    list_filter = ('name',)

@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'message', 'template', 'recipients', 'sent')
    list_filter = ('subject', 'message', 'recipients', 'template', 'sent' )
    actions = ['send_email_from_contact',]

    def send_email_from_contact(self, request, queryset):
        queryset.update(sent=F('sent') + 1)
        for q in queryset:
            context = {
                'QR': 'http://www.aaaimx.org/certificates/?id=bf836798-ab69-4342-9f9d-d3cb9d0a61b7',
                'drive': 'https://drive.google.com/file/d/1JvhdgfrrJtBButU0scWcT82id4x1AC1_/view?usp=drivesdk',
                'thumbnail': 'https://drive.google.com/uc?id=1JvhdgfrrJtBButU0scWcT82id4x1AC1_',
                'uuid': 'bf836798-ab69-4342-9f9d-d3cb9d0a61b7',
                'email': 'rnovelo.cruz98@gmail.com'
            }
            template = parse_template(context, q.template)
            send_email(q.subject, q.message, q.recipients, template)
    send_email_from_contact.short_description = "Send selected emails"