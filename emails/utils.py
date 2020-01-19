
from django.conf import settings

def parse_template(context, template):
    message_content = str(open(settings.BASE_DIR + template.file.url, 'r').read())
    for key in template.context:
        message_content = message_content.replace('{{' + key + '}}', context[key])
    return message_content