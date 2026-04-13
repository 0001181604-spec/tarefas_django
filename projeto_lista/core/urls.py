from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.meu_login, name='login'),
    path('tarefas/', views.tarefa_list, name='tarefa-list'),  
    path('logout/', views.meu_logout, name='logout'), 
    path('tarefas/nova/', views.tarefa_create, name='tarefa-create'),
path('tarefas/<int:pk>/editar/', views.tarefa_update, name='tarefa-edit'),
path('tarefas/<int:pk>/excluir/', views.tarefa_delete, name='tarefa-delete'),
path('categorias/', views.categoria_list, name='categoria-list'),
path('categorias/nova/', views.categoria_create, name='categoria-create'),
path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria-edit'),
path('categorias/<int:pk>/excluir/', views.categoria_delete, name='categoria-delete'),
path('prioridades/', views.prioridade_list, name='prioridade-list'),
path('prioridades/nova/', views.prioridade_create, name='prioridade-create'),
path('prioridades/<int:pk>/editar/', views.prioridade_update, name='prioridade-edit'),
path('prioridades/<int:pk>/excluir/', views.prioridade_delete, name='prioridade-delete'),
]
