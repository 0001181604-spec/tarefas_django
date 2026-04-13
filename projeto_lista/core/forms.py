from django import forms
from .models import Tarefa
from .models import Tarefa, Categoria, Prioridade

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class PrioridadeForm(forms.ModelForm):
    class Meta:
        model = Prioridade
        fields = ['nivel']
        
class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prazo', 'status', 'categoria', 'prioridade']
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}),
        }
