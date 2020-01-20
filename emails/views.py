from .models import Email, Template
from rest_framework import viewsets
from .serializers import TemplateSerializer, EmailSerializer

# ViewSets define the view behavior.
class EmailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Emails to be viewed or edited.
    """
    queryset = Email.objects.all().order_by('-date_created')
    serializer_class = EmailSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Templates to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
