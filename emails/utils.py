
from django.conf import settings

def parse_template(context, template):
    path = settings.BASE_DIR + '/templates/email/' + template.file_name
    message_content = str(open(path, 'r').read())
    for key in template.keys:
        message_content = message_content.replace('{{' + key + '}}', context[key])
    return message_content