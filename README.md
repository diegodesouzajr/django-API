# django-API
Aplicação Django (backend) para login e cadastro de usuário.

Ao acessar a pasta projeto, instalar as bibliotecas através do arquivo requirements.py

Utilizar o comando "python manage.py runserver" para iniciar o sistema.

O link inicial "http://127.0.0.1:8000/" levará ao menu do sistema.
No menu você encontrará duas opções, login e cadastro.

Na tela de cadastro, você vai cadastrar seu usuário, os campos nome, email, senha, cpf, pis são obrigatórios.
Os campo cpf, pis e email não devem ser repetidos.

Na tela de login você deve inserir o cpf e senha cadastrado na tela de cadastro.

Após o login, o sistema apresentará a lista de usuário, podendo realizar um novo cadastro, edição ou exclusão de usuários.


Ferramentas utilizadas:
Django 3.1.7
Banco de dados sqlite3

O login é feito pelo método "authenticate", da biblioteca "django.contrib.auth"
