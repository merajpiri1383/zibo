from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from threading import Thread
def send_async_email(user):
    context = {"code" : user.activation_code}
    html = render_to_string("email/send_activation.html",context=context)
    message = EmailMultiAlternatives(
        subject="Activation Code",
        from_email="1383merajpiri@gmail.com",
        to=[user.email]
    )
    message.attach_alternative(html, "text/html")
    message.send()
def send_email(user):
    task = Thread(target=send_async_email,args=[user]) 
    task.start()
def send_password_reset_async(user) :
    html = render_to_string("email/send_password.html",{"code":user.activation_code})
    message = EmailMultiAlternatives(
        subject=" Rest Password ",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    message.attach_alternative(html,mimetype="text/html")
    message.send()
def send_password_reset_email(user) :
    task = Thread(target=send_password_reset_async,args=[user])
    task.start()