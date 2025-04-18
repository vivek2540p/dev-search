from .models import Profiles,Skill
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def searchProfiles(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    skills=Skill.objects.filter(name__iexact=search_query)
    profiles = Profiles.objects.distinct().filter(Q(name__icontains=search_query) | Q(skill__in=skills))
    return profiles,search_query

def paginateProfiles(request,profiles,results):
    paginator=Paginator(profiles,results)
    try:
        page=request.GET.get('page')
        profiles= paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles= paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        profiles= paginator.page(page)
    leftIndex=(int(page)-1)
    if leftIndex<1:
        leftIndex=1
    rightIndex= int(page)+2
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1
    custome_range=range(leftIndex,rightIndex)
    return custome_range,profiles