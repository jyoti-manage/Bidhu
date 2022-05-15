from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
   
    path('',views.index,name = 'index'),
    path('register/', views.register_page,name='register'),
    path('login/', views.login_page,name='login'),
    path('login/', views.logout_page,name='logout'),
    path('main/contact/', views.contact,name='contact'),
    path('searchList/',views.searchList,name='searchList')
    
]