from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.meu_login, name='login'),
    path('tarefas/', views.tarefa_list, name='tarefa-list'),  
    path('logout/', views.meu_logout, name='logout'), 
    path('tarefas/nova/', views.tarefa_create, name='tarefa-create'),
path('tarefas/<int:pk>/editar/', views.tarefa_update, name='tarefa-edit'),
path('tarefas/<int:pk>/excluir/', views.tarefa_delete, name='tarefa-delete'),
]
