# jobapp/utils.py

from django.core.mail import send_mail

def send_notification(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        None,
        [recipient_email],
        fail_silently=False,
    )
