from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profiles,Skill,Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email','username', 'password1', 'password2']
        labels={
            'first_name':'Name',
            }
        
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        for name,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields=['name','email','username','location','profile_image','short_intro','bio','social_github','social_twitter','social_linkedin','social_youtube','social_website']
        
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args, **kwargs)
        for name,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
            
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields=['name','description']
    
    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args, **kwargs)
        for name,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
        
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields=['name','email','subject','body']
    
    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args, **kwargs)
        for name,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})