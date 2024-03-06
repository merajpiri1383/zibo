from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from time import sleep
from django.dispatch import receiver
from threading import Thread
def delete_user_asycn(instance,created):
    sleep(120)
    try : 
        user = get_user_model().objects.get(email=instance.email)
        if not user.is_active : 
            user.delete()
    except : pass 
@receiver(post_save,sender=get_user_model())
def delete_in_active_user_after_120(sender,instance,created,**kwargs) :
    task = Thread(target=delete_user_asycn,args=[instance,created])
    task.start()