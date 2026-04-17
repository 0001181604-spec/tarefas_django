from rest_framework import serializers
from .models import Tarefa, Categoria, Prioridade

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PrioridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridade
        fields = '__all__'

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'