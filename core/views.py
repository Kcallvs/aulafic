from django.shortcuts import render, redirect
from .models import Area, PublicoAlvo, Curso, Usuario
from .forms import AreaForm, PublicoAlvoForm, CursoForm
from django.contrib.auth import authenticate, login, logout

from .models import Usuario
from .forms import UsuarioFormCadastro

from django.contrib.auth.decorators import login_required  

@login_required
def perfil(request):
    return render(request, 'privado/perfil.html')

def cadastro(request):
    form = UsuarioFormCadastro(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'privado/cadastro.html', context)

def autenticar(request):

    if request.POST:
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request,username= username, password= password)
        if user is not None:
            login(request,user)
            return redirect('perfil')
        else:
            return render(request, 'privado/login.html')
    else: 
        return render(request, 'privado/login.html')

def sair(request):
    logout(request)
    return redirect('index')
    

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def curso_galeria(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'curso_galeria.html',context)

def curso_detalhe(request):
    curso = Curso.objects.get(pk=id)
    context = {
        'curso': curso
    }
    return render(request, 'curso_detalhe.html',context)

@login_required
def area_listar(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }
    #return render(request, 'areas.html', context)
    return render(request, 'privado/areas.html', context)

@login_required
def area_cadastrar(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('area_listar')
    context = {
        'form': form
    }
    #return render(request, 'area_cadastrar.html', context)
    return render(request, 'privado/area_cadastrar.html', context)

@login_required
def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('area_listar')
    context = {
        'form': form
    }
    #return render(request, 'area_cadastrar.html', context)
    return render(request, 'privado/area_cadastrar.html', context)

@login_required
def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area_listar')

@login_required
def publicoalvo_listar(request):
    publicoalvos = PublicoAlvo.objects.all()
    context = {
        'publicoalvos': publicoalvos
    }
    return render(request, 'privado/publicoalvos.html', context)

@login_required
def publicoalvo_cadastrar(request):
    form = PublicoAlvoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicoalvo_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/publicoalvo_cadastrar.html', context)

@login_required
def publicoalvo_editar(request, id):
    publicoalvo = PublicoAlvo.objects.get(pk=id)
    form = PublicoAlvoForm(request.POST or None, instance=publicoalvo)
    if form.is_valid():
        form.save()
        return redirect('publicoalvo_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/publicoalvo_cadastrar.html', context)

@login_required
def publicoalvo_remover(request, id):
    publicoalvo = PublicoAlvo.objects.get(pk=id)
    publicoalvo.delete()
    return redirect('publicoalvo_listar')

@login_required
def curso_listar(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'privado/cursos.html', context)

@login_required
def curso_cadastrar(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/curso_cadastrar.html', context)
