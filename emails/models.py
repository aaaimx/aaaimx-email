from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Email(models.Model):
    subject = models.CharField(default="Good news!!", max_length=200, blank=True)
    html_message = models.CharField(default=None, max_length=200, blank=True)
    message = models.CharField(default=None, max_length=200, blank=True)
    recipients = ArrayField(models.CharField(
        default="", max_length=200, null=True), size=20, default=list)