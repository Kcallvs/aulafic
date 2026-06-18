from django.shortcuts import render, redirect
from .models import Area, PublicoAlvo, Curso, Usuario
from .forms import AreaForm, PublicoAlvoForm, CursoForm
from django.contrib.auth import authenticate, login

# Usuários
from .models import Usuario
from .forms import UsuarioFormCadastro

def cadastro(request):
    form = UsuarioFormCadastro(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'cadastro.html', context)

def autenticar(request):
    if request.POST:
     username= request.POST['username']
     password= request.POST['password']
     user = authenticate(request,username= username, password= password)
    
    if user is not None:
            login(request,user)
            return redirect('index')
    else:
            return render(request, 'login.html')
    

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def curso_galeria(request):
    return render(request, 'curso_galeria.html')

def area_listar(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }
    #return render(request, 'areas.html', context)
    return render(request, 'privado/areas.html', context)

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

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area_listar')





def publicoalvo_listar(request):
    publicoalvos = PublicoAlvo.objects.all()
    context = {
        'publicoalvos': publicoalvos
    }
    return render(request, 'privado/publicoalvos.html', context)

def publicoalvo_cadastrar(request):
    form = PublicoAlvoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicoalvo_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/publicoalvo_cadastrar.html', context)

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

def publicoalvo_remover(request, id):
    publicoalvo = PublicoAlvo.objects.get(pk=id)
    publicoalvo.delete()
    return redirect('publicoalvo_listar')

def curso_listar(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'privado/cursos.html', context)

def curso_cadastrar(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso_listar')
    context = {
        'form': form
    }
    return render(request, 'privado/curso_cadastrar.html', context)
