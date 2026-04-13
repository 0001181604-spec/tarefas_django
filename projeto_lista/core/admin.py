from django.contrib import admin
from .models import Tarefa, Categoria, Prioridade

admin.site.register(Tarefa)
admin.site.register(Categoria)
admin.site.register(Prioridade)