from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import Tarefa, Categoria, Prioridade
from .forms import TarefaForm, CategoriaForm, PrioridadeForm
def meu_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Bem-vindo!')
            return redirect('tarefa-list')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'core/login.html')

def meu_logout(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('login')

@login_required
def tarefa_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'core/tarefa_list.html', {'tarefas': tarefas})

@login_required
def tarefa_create(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('tarefa-list')
    else:
        form = TarefaForm()
    return render(request, 'core/tarefa_form.html', {'form': form})

@login_required
def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('tarefa-list')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/tarefa_form.html', {'form': form})

@login_required
def tarefa_delete(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('tarefa-list')
    return render(request, 'core/tarefa_confirm_delete.html', {'tarefa': tarefa})     
  
  # CRUD Categoria
@login_required
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/categoria_list.html', {'categorias': categorias})

@login_required
def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('categoria-list')
    else:
        form = CategoriaForm()
    return render(request, 'core/categoria_form.html', {'form': form})

@login_required
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('categoria-list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'core/categoria_form.html', {'form': form})

@login_required
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('categoria-list')
    return render(request, 'core/categoria_confirm_delete.html', {'categoria': categoria})

# CRUD Prioridade
@login_required
def prioridade_list(request):
    prioridades = Prioridade.objects.all()
    return render(request, 'core/prioridade_list.html', {'prioridades': prioridades})

@login_required
def prioridade_create(request):
    if request.method == 'POST':
        form = PrioridadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prioridade criada com sucesso!')
            return redirect('prioridade-list')
    else:
        form = PrioridadeForm()
    return render(request, 'core/prioridade_form.html', {'form': form})

@login_required
def prioridade_update(request, pk):
    prioridade = get_object_or_404(Prioridade, pk=pk)
    if request.method == 'POST':
        form = PrioridadeForm(request.POST, instance=prioridade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prioridade atualizada com sucesso!')
            return redirect('prioridade-list')
    else:
        form = PrioridadeForm(instance=prioridade)
    return render(request, 'core/prioridade_form.html', {'form': form})

@login_required
def prioridade_delete(request, pk):
    prioridade = get_object_or_404(Prioridade, pk=pk)
    if request.method == 'POST':
        prioridade.delete()
        messages.success(request, 'Prioridade excluída com sucesso!')
        return redirect('prioridade-list')
    return render(request, 'core/prioridade_confirm_delete.html', {'prioridade': prioridade})
