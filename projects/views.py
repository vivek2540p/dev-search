from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm,ReviewForm
from .utils import searchProjects,paginateProject

def projects(request):
    projects,search_query=searchProjects(request)
    projects,custome_range=paginateProject(request,projects,3)
    context={
        'projects':projects,
        'search_query':search_query,
        'custome_range':custome_range,
    }
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=='POST':
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.owner=request.user.profiles
            review.project=project
            try:
                review.save()
            except:
                messages.error(request,"Already add a review!")
            project.getVoteCount
            return redirect('project',pk=pk)
    form=ReviewForm()
    context={
        'project':project,
        'form':form
    }
    return render(request,'projects/single_project.html',context)



@login_required(login_url="login")
def createProject(request):
    profile=request.user.profiles
    form= ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')
    context={'form':form}
    return render(request,'projects/project_form.html',context)



@login_required(login_url="login")
def updateProject(request,pk):
    projectObj=Project.objects.get(id=pk)
    form= ProjectForm(instance=projectObj)
    
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=projectObj)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url="login")
def deleteProject(request,pk):
    projectObj=Project.objects.get(id=pk)
    projectObj.delete()
    return redirect('account')