from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profiles(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField( max_length=200, null=True, blank=True)
    username=models.CharField( max_length=200, null=True, blank=True)
    location=models.CharField( max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=500, null=True, blank=True)
    profile_image=models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/user-default.png')
    short_intro= models.CharField(max_length=200, null=True, blank=True)
    bio= models.TextField(null=True, blank=True)
    social_github= models.CharField(max_length=200, null=True, blank=True)
    social_twitter= models.CharField(max_length=200, null=True, blank=True)
    social_linkedin= models.CharField(max_length=200, null=True, blank=True)
    social_youtube= models.CharField(max_length=200, null=True, blank=True)
    social_website= models.CharField(max_length=200, null=True, blank=True)
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering=['-created']

class Skill(models.Model):
    owner=models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True, blank=True)
    description= models.TextField( null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    sender=models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True, blank=True)
    receiver=models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True, blank=True,related_name="messages")
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(max_length=500, null=True, blank=True)
    subject=models.CharField(max_length=200, null=True, blank=True)
    body=models.TextField(null=True, blank=True)
    is_read=models.BooleanField(default=False, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.subject
    
    @property
    def read_message(self):
        self.is_read=True
        self.save()
    
    class Meta:
        ordering=['is_read','-created']
    
    
    
