from django.core.mail import send_mail
from celery.decorators import task
from celery.result import AsyncResult
import os

@task(name="send_email")
def send_email(subject, message, to, template=None):
    send_mail(subject, message, os.environ.get('EMAIL_HOST_USER'), to, fail_silently=True, html_message=template)