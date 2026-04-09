# core/models.py
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'categorias'


class Prioridade(models.Model):
    NIVEL_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES)

    def __str__(self):
        return self.get_nivel_display()

    class Meta:
        verbose_name_plural = 'prioridades'


class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    prazo = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    prioridade = models.ForeignKey(Prioridade, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'tarefas'