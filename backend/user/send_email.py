from django.core.mail import EmailMultiAlternatives
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from threading import Thread
def send_async_email(user,request):
    context = {
        "url" : request.build_absolute_uri(reverse("activate",args=[user.activation_code]))
    }
    html = render_to_string("email/send_activation.html",context=context)
    message = EmailMultiAlternatives(
        subject="Activation Code",
        from_email="1383merajpiri@gmail.com",
        to=[user.email]
    )
    message.attach_alternative(html, "text/html")
    message.send()
def send_email(user,request):
    task = Thread(target=send_async_email,args=[user,request])
    task.start()