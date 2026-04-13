from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
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