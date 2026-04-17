from rest_framework import viewsets, permissions
from .models import Tarefa, Categoria, Prioridade
from .serializers import TarefaSerializer, CategoriaSerializer, PrioridadeSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

class PrioridadeViewSet(viewsets.ModelViewSet):
    queryset = Prioridade.objects.all()
    serializer_class = PrioridadeSerializer
    permission_classes = [permissions.IsAuthenticated]