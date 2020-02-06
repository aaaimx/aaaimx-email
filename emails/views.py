from .models import Email, Template
from .serializers import TemplateSerializer, EmailSerializer
from .utils import parse_template
from .tasks import send_email

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

# ViewSets define the view behavior.
class EmailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Emails to be viewed or edited.
    """
    queryset = Email.objects.all().order_by('-pk')
    serializer_class = EmailSerializer

    def send_email(self, data):
        pk = data.get('template', None)
        if pk is not None:
            template = Template.objects.get(pk=pk)
            tmp = parse_template(data['context'], template)
            send_email(data['subject'], data['message'], data['recipients'], tmp)
        else:
            send_email(data['subject'], data['message'], data['recipients'], None)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.send_email(request.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}



class TemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Templates to be viewed or edited.
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
