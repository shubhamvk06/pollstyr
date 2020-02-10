from django.urls import path
from . import views

app_name='polls'
urlpatterns=[
    
    path('<int:question_id>/', views.details, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.pages, name='pages'),   
    path('index', views.index, name='index'),
    path('voter',views.voter, name='voter') 


]