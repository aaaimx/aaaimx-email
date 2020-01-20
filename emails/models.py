from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField, JSONField
from datetime import datetime

class Template(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default=uuid4, primary_key=True, editable=True, max_length=200)
    file = models.FileField(upload_to="templates", null=True, blank=True)
    keys = ArrayField(models.CharField(
        default="", max_length=200, null=True), size=20, default=list)

# Create your models here.
class Email(models.Model):
    def __str__(self):
        return self.subject
    template = models.ForeignKey(Template, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(default="", max_length=200, blank=True)
    message = models.CharField(default="", max_length=200, blank=True)
    sent = models.IntegerField(default=0, blank=True)
    context = JSONField()
    recipients = ArrayField(models.CharField(
        default="", max_length=200, null=True), size=20, default=list)
