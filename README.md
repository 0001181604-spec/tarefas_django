# Sistema de Tarefas Diárias

Aplicação web desenvolvida com Django para gerenciamento de tarefas do dia a dia. O sistema permite criar, editar e excluir tarefas, organizando-as por categoria e prioridade, com autenticação manual e API REST.

## Funcionalidades

- Login e logout com autenticação manual
- CRUD completo de Tarefas, Categorias e Prioridades
- API REST para acesso aos dados em JSON
- Mensagens de feedback para o usuário
- Rotas protegidas — apenas usuários autenticados acessam o sistema

## Tecnologias utilizadas

- Python 3.13
- Django 6.0
- Django REST Framework
- SQLite

## Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/0001181604-spec/tarefas_django.git
cd tarefas_django
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install django djangorestframework
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 6. Rode o servidor
```bash
python manage.py runserver
```

### 7. Acesse no navegador
- Interface web: http://127.0.0.1:8000
- API REST: http://127.0.0.1:8000/api/
- Admin: http://127.0.0.1:8000/admin/