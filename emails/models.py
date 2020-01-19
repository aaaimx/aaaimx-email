from django.db import models
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField


class Template(models.Model):
    def __str__(self):
        return self.name
    file = models.FileField(upload_to="templates", null=True, blank=True)
    name = models.CharField(default="", max_length=200, blank=True)
    context = ArrayField(models.CharField(
        default="", max_length=200, null=True), size=20, default=list)

# Create your models here.
class Email(models.Model):
    template = models.ForeignKey(Template, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(default="", max_length=200, blank=True)
    message = models.CharField(default="", max_length=200, blank=True)
    sent = models.IntegerField(default=0, blank=True)
    recipients = ArrayField(models.CharField(
        default="", max_length=200, null=True), size=20, default=list)
