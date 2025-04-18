from django.contrib.auth.models import User
from .models import Profiles
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
# @receiver(post_save,sender=Profiles)
def createProfile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile=Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email
        )
        subject = 'Welecome to Devsearch'
        message = 'Registeration is successfully done.'
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email],
        #     fail_silently=False
        # )
    
    
def deleteProfile(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.username=str(profile.username)
        user.email=profile.email
        user.save()
    
post_save.connect(createProfile,sender=User)  
post_save.connect(updateUser,sender=Profiles)  
post_delete.connect(deleteProfile,sender=Profiles)  