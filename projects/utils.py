from .models import Project,Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from langchain_google_genai import ChatGoogleGenerativeAI
from django.conf import settings

def searchProjects(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    tags=Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(tags__in=tags))
    return projects,search_query

def paginateProject(request,projects,results):

    paginator=Paginator(projects,results)
    try:
        page=request.GET.get('page')
        projects= paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects= paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        projects= paginator.page(page)
    leftIndex=(int(page)-1)
    if leftIndex<1:
        leftIndex=1
    rightIndex= int(page)+2
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1
    custome_range=range(leftIndex,rightIndex)
    return projects,custome_range

def chatbot(query,context):
    print("KEY :",settings.GEMINI_API_KEY)
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",google_api_key=settings.GEMINI_API_KEY)
    prompt = """ You are a helpful and knowledgeable project assistant.
    Below is the context of a software project followed by a user's question.Answer the following question based only on provided context.The agent can also respond to project-related queries using its built-in knowledge base.Use the context to generate a helpful, accurate, and concise answer. Keep the response short and relevant .For general questions or greetings, respond concisely.
    <context>
    """+context+"""
    </context>
    User Question:
    """+query+"""

    Instructions:
    - Use only the information provided in the context.
    - If something is unclear or missing, politely mention that to the user.
    - Be clear, friendly, and professional in tone.
    - Keep the response short and relevant.
    """
    response = llm.invoke(prompt)
    return response.content
    