from django.forms import ModelForm
from django import forms
from .models import Project,Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image','demo_link','source_link','tags']
        widgets={
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Project Title'})
        print("12345")
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})
            
class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['value','body']
        labels={
            'value':'Place Your Vote',
            'body': 'Add a Comment',
        }
    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)
        
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'input'})