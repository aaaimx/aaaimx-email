from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'contact@aaaimx.org',
    ['rnovelo.cruz98@gmail.com'],
    fail_silently=True,)