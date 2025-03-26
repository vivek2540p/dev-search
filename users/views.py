from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Profiles,Message
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,SkillForm,MessageForm
from .utils import searchProfiles,paginateProfiles
# Create your views here.

def loginPage(request):
    page='login'
    context={
        'page':page
    }
    if request.user.is_authenticated :
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request,"Password is incorrect")
    return render(request,'users/login_register.html',context)

def logoutUser(request):
    logout(request)
    messages.info(request,"User Logged out!")
    return redirect('login')

def registerUser(request):
    if request.user.is_authenticated :
        return redirect('profiles')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,"Registerd Successfully")
            login(request, user)
            return redirect('edit-account')
            
    page='register'
    form=CustomUserCreationForm()
    context={
        'page':page,
        'form':form
    }
    return render(request,'users/login_register.html',context)

def profiles(request):
    profiles=None
    profiles,search_query=searchProfiles(request)
    custome_range,profiles=paginateProfiles(request,profiles,3)
    if not request.user.is_anonymous:
        profiles=filter(lambda x:x.id!=request.user.profiles.id,profiles)
    context={
        'profiles': profiles,
        'search_query':search_query,
        'custome_range':custome_range
    }
    return render(request, 'users/profiles.html',context)

def userProfile(request,pk):
    profile = Profiles.objects.get(id=pk)
    context={
        'profile': profile
    }
    return render(request,'users/user-profile.html',context)

@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profiles
    context={
        'profile':profile
    }
    return render(request,'users/account.html',context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profiles
    form=ProfileForm(instance=profile)
    context={
        'form':form
    }
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request,'users/profile_form.html',context)


@login_required(login_url='login')
def addSkill(request):
    profile = request.user.profiles
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')
    return render(request, 'users/skill_form.html', {'form': form})


@login_required(login_url='login')
def editSkill(request,pk):
    profile = request.user.profiles
    skills = profile.skill_set.get(id=pk)
    form =SkillForm(instance=skills)
    if request.method == 'POST':
        form = SkillForm(request.POST,request.FILES,instance=skills)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        'form':form
    }
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request,pk):
    profile = request.user.profiles
    skills = profile.skill_set.get(id=pk)
    skills.delete()
    return redirect('account')

def inbox(request):
    profile=request.user.profiles
    messages = profile.messages.all()
    unread= profile.messages.filter(is_read=False).count()
    context = {
        'userMessages':messages,
        'unread':unread
    }
    return render(request,'users/inbox.html',context)

def readMessage(request,pk):
    profile = request.user.profiles
    message = profile.messages.get(id=pk)
    message.read_message
    context={
        'message':message
    }
    return render(request, 'users/message.html',context)

def sendMessage(request):
    form =MessageForm()
    prev=request.GET['next']
    profile=None
    if not request.user.is_anonymous:
        profile=request.user.profiles
    receiver_id=request.GET['id']
    receiver=Profiles.objects.get(id=receiver_id)
    print(profile,receiver,"11")
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message= form.save(commit=False)
            message.sender=profile
            message.receiver=receiver
            message.save()
            return redirect(prev)
    context={
        'form':form,
        'prev':prev
    }
    return render(request,'users/message_form.html',context)
    
    