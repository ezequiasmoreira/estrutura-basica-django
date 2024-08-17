
Configuração

Para verificar se o PIP está instalado no seu sistema, execute um dos seguintes comandos no Prompt de Comando:

python -m pip --version

ou

python3 -m pip --version

Reinstalar o PIP (se necessário)
Se o PIP não estiver instalado, você pode instalá-lo manualmente. Primeiro, baixe o script get-pip.py 
usando o comando:

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Baixar o Python
Se ainda não tiver o Python instalado, faça o download a partir do site oficial:

Download Python: https://www.python.org/downloads/

Adicionar o Python às variáveis de ambiente

Durante a instalação do Python, certifique-se de marcar a opção "Add Python to PATH" para adicionar
 o Python às variáveis de ambiente do sistema, o que permitirá que você o execute diretamente no 
 Prompt de Comando.

 *******************************************************************************************************
1. Configuração Inicial do Projeto Django
Primeiro, você deve ter o Django instalado em seu ambiente de desenvolvimento. Se ainda não tiver, 
instale usando:

pip install django

Crie um novo projeto Django:

django-admin startproject mysite
cd mysite
Em seguida, crie um aplicativo Django dentro do projeto:

python manage.py startapp main

***************************************************************************************************

2. Estrutura de Diretórios
A estrutura básica do projeto será a seguinte:

mysite/
│
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── main/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── about.html
│   │   └── contact.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── db.sqlite3

***************************************************************************************************

3. Configuração do settings.py
No arquivo mysite/settings.py, adicione main ao INSTALLED_APPS:

INSTALLED_APPS = [
    ...
    'main',
]

***************************************************************************************************

4. Definição de URLs
Edite o arquivo mysite/urls.py para incluir as URLs do aplicativo main:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
Agora, crie um arquivo urls.py dentro da pasta main:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

***************************************************************************************************

5. Criação das Views
No arquivo views.py dentro de main, crie as funções de visualização para as páginas:

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

***************************************************************************************************

6. Criação dos Templates
Na pasta main/templates/, crie os arquivos HTML:

index.html

{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<body>
    <h1>Welcome to Our Website</h1>
    <nav><a href="{% url 'home' %}">Home</a><a href="{% url 'about' %}">About</a><a
            href="{% url 'contact' %}">Contact</a></nav>
    <p>This is the homepage.</p>
</body>

</html>

***************************************************************************************************

about.html

{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<body>
    <h1>About Us</h1>
    <nav><a href="{% url 'home' %}">Home</a><a href="{% url 'about' %}">About</a><a
            href="{% url 'contact' %}">Contact</a></nav>
    <p>This is the about page.</p>
</body>

</html>

***************************************************************************************************

contact.html

{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>

<body>
    <h1>Contact Us</h1>
    <nav><a href="{% url 'home' %}">Home</a><a href="{% url 'about' %}">About</a><a
            href="{% url 'contact' %}">Contact</a></nav>
    <p>This is the contact page.</p>
</body>

</html>

***************************************************************************************************

7. Adicionando Estilos CSS
Na pasta main/static/css/, crie o arquivo styles.css:

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

h1 {
    background-color: #333;
    color: white;
    padding: 10px;
    text-align: center;
}

nav {
    margin: 10px;
    text-align: center;
}

nava {
    margin: 015px;
    text-decoration: none;
    color: #333;
}

nava:hover {
    color: #007BFF;
}

p {
    padding: 10px;
    text-align: center;
}

***************************************************************************************************

8. Aplicar as Migrações
Para aplicar as migrações, execute o seguinte comando:

python manage.py migrate

***************************************************************************************************

9. Rodando o Servidor
Execute o servidor para visualizar o site:

python manage.py runserver
Acesse http://127.0.0.1:8000/ no navegador para ver o site em funcionamento.

***************************************************************************************************

10. Documentação
Processo de Desenvolvimento:

Criação do Projeto: O projeto foi iniciado criando-se um novo projeto Django e um aplicativo dentro dele.
Configuração do Ambiente: Configuramos o ambiente, incluindo as URLs e as views básicas.
Desenvolvimento de Templates: Criamos os arquivos HTML para cada uma das páginas.
Adição de Estilos: Um arquivo CSS foi adicionado para estilizar as páginas de forma consistente.
Testes: O servidor foi iniciado para testar as funcionalidades e garantir que todas as páginas estivessem 
acessíveis.

Funcionalidades Implementadas:

Página Inicial (Home): Apresenta uma visão geral do site com navegação para outras páginas.
Página Sobre (About): Descreve informações sobre o site ou a organização.
Página de Contato (Contact): Fornece informações de contato ou um formulário para entrar em contato.

