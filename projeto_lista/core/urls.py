from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.meu_login, name='login'),
    path('tarefas/', views.tarefa_list, name='tarefa-list'),  
    path('logout/', views.meu_logout, name='logout'), 
]
