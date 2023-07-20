from django.conf import settings
from django.core.mail import send_mail
from .models import Owner_Email


def send_email_to_owner(sub, msg):
    from_email = settings.EMAIL_HOST_USER
    recipient_list = list(str(i.email) for i in Owner_Email.objects.all())
    return send_mail(sub, msg, from_email, recipient_list)


def send_email_to_user(sub, msg, email):
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    return send_mail(sub, msg, from_email, recipient_list)