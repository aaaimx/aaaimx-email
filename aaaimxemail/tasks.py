from celery.decorators import task


@task(name="send_email")
def send_email(context):
    send_mail(
    'Subject here',
    'Here is the message.',
    'contact@aaaimx.org',
    ['rnovelo.cruz98@gmail.com'],
    fail_silently=True,)