from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from sistema.forms import UsuarioForm
from sistema.models import Usuario


def menu(request):
    return render(request, 'menu.html')


def usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()

                request_form = {
                    'username': request.POST.get('cpf'),
                    'email': request.POST.get('email'),
                    'password1': request.POST.get('senha'),
                    'password2': request.POST.get('senha'),
                }

                form_auth_user = UserCreationForm(request_form)

                if form_auth_user.is_valid():
                    form_auth_user.save()

                return redirect("/show")
            except:
                pass
    else:
        form = UsuarioForm()

    return render(request, 'index.html', {'form': form})


def show(request):
    usuarios = Usuario.objects.all()
    return render(request, "show.html", {'usuarios': usuarios})


def edit(request, id):
    usuario = Usuario.objects.get(usuario_id=id)
    return render(request, 'edit.html', {'usuario': usuario})


def update(request, id):
    usuario = Usuario.objects.get(usuario_id=id)
    form = UsuarioForm(request.POST, instance=usuario)
    if form.is_valid():
        form.save()

        if request.POST['cpf'] and request.POST['senha']:
            user = User.objects.get(username=request.POST['cpf'])
            user.set_password(request.POST['senha'])
            user.save()

        return redirect("/show")
    return render(request, 'edit.html', {'usuario': usuario})


def destroy(request, id):
    usuario = Usuario.objects.get(usuario_id=id)
    usuario.delete()
    return redirect("/show")


def cadastro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'menu.html')
            except:
                pass
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})


def login(request):

    if request.method == "POST":
        try:
            username = request.POST["cpf"]
            password = request.POST["senha"]

            usuario = authenticate(request, username=username, password=password)
        except:
            usuario = None

        if usuario:
            return redirect('/show')

    return render(request, 'login.html')