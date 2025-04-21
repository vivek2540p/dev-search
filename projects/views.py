from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm,ReviewForm
from .utils import searchProjects,paginateProject,chatbot

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
    review_user = [review.owner.user.id for review in project.review_set.all()]
    print(review_user)
    context={
        'project':project,
        'form':form,
        'review_user':review_user
    }
    return render(request,'projects/single_project.html',context)



@login_required(login_url="login")
def createProject(request):
    profile = request.user.profiles
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)



@login_required(login_url="login")
def updateProject(request,pk):
    projectObj=Project.objects.get(id=pk)
    form= ProjectForm(instance=projectObj)
    
    if request.method=='POST':
        # newtags = request.POST.get('newtags').replace(',',  " ").split()
        form=ProjectForm(request.POST,request.FILES,instance=projectObj)
        if form.is_valid():
            form.save()
            # for tag in newtags:
            #     tag ,created= Tag.objects.get_or_create(name=tag)
            #     projectObj.tags.add(tag)
            projectObj.save()
            return redirect('account')
    context={'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url="login")
def deleteProject(request,pk):
    projectObj=Project.objects.get(id=pk)
    projectObj.delete()
    return redirect('account')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message", "")
        pk = data.get("project", "")
        project =Project.objects.get(id=pk)
        # project.tags.se
        print(project.description,project.title)
        print(project.tags.all())
        context = """ 
        Project Name : """ +  project.title +"""
        Project Description : """ +  project.description +"""
        Languages and FrameWork  : """ +  ", ".join([tag.name for tag in project.tags.all()]) +"""
        """
        # Placeholder bot logic — replace with your actual bot logic
        bot_reply = chatbot(query=user_input,context=context)

        return JsonResponse({"response": bot_reply})