from django.urls import path
from . import views

urlpatterns=[
    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>',views.userProfile,name='user-profile'),
    
    
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('account/',views.userAccount,name="account"),
    path('edit-account/',views.editAccount,name="edit-account"),
    
    
    path('add-skill/',views.addSkill,name="add-skill"),
    path('edit-skill/<str:pk>',views.editSkill,name="edit-skill"),
    path('delete-skill/<str:pk>',views.deleteSkill,name="delete-skill"),
    
    
    path('inbox/',views.inbox,name="inbox"),
    path('read-message/<str:pk>',views.readMessage,name="read-message"),
    path('send-message/',views.sendMessage,name="send-message"),
    
]