from django.urls import path
from .views import *

urlpatterns = [
    path('perfil/', perfil, name='perfil'),
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('curso_galeria/', curso_galeria, name='curso_galeria'),
    path('curso_detalhe/<int:id>/', curso_detalhe, name='curso_detalhe'),
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', autenticar, name="login"),
    path('sair/', sair, name="sair"),

    path('area_listar', area_listar, name='area_listar'),
    path('area_cadastrar', area_cadastrar, name='area_cadastrar'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),

    path('publicoalvo_listar/', publicoalvo_listar, name='publicoalvo_listar'),
    path('publicoalvo_cadastrar/', publicoalvo_cadastrar, name='publicoalvo_cadastrar'),
    path('publicoalvo_editar/<int:id>/', publicoalvo_editar, name='publicoalvo_editar'),
    path('publicoalvo_remover/<int:id>/', publicoalvo_remover, name='publicoalvo_remover'),

    path('curso_listar/', curso_listar, name='curso_listar'),
    path('curso_cadastrar/', curso_cadastrar, name='curso_cadastrar'),

]