from django.forms import ModelForm
from django import forms
from .models import Project,Review, Tag

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','featured_image','demo_link','source_link','tags']
        widgets={
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        if self.instance and self.instance.pk:
            # Editing existing project — show only selected tags
            self.fields['tags'].queryset = self.instance.tags.all()
        else:
            # Adding new project — show all available tags
            self.fields['tags'].queryset = Tag.objects.all()
        
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Project Title'})
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