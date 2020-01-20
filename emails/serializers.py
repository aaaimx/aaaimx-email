from rest_framework import serializers
from .models import Email, Template

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        exclude = []

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        exclude = []