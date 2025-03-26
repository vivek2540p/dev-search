from django.db import models
import uuid
from users.models import Profiles
# Create your models here.

class Project(models.Model):
    owner= models.ForeignKey(Profiles, on_delete=models.CASCADE,null=True,blank=True ) 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    featured_image=models.ImageField( null=True,blank=True,default="default.jpg")
    demo_link=models.CharField( max_length=200,null=True,blank=True)
    source_link=models.CharField( max_length=200,null=True,blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.title
    
    @property
    def updateVote(self):
        self.vote_total = self.vote_total + 1
    
    class Meta:
        ordering=['-vote_ratio','-vote_total']
     
    @property   
    def getVoteCount(self):
        reviews=self.review_set.all()
        upVotes=reviews.filter(value='up').count() 
        totalVotes=reviews.count()
        ratio=(upVotes/totalVotes)*100
        self.vote_total=totalVotes
        self.vote_ratio=ratio
        self.save()
        
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
        )
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    value=models.CharField( max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.value
    class Meta:
        unique_together = [['owner', 'project']]
        ordering=['-created']
    
class Tag(models.Model):
    name = models.CharField( max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.name