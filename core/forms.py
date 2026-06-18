from django import forms
from .models import Area, PublicoAlvo, Curso, Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioFormCadastro(UserCreationForm):
    class Meta:
         model = Usuario
         fields = ['cpf', 'email','nascimento', 'first_name', 'last_name', 'username']
     
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoAlvoForm(forms.ModelForm):
    class Meta:
        model = PublicoAlvo
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta: 
        model = Curso
        fields = [
            'titulo', 
            'descricao', 
            'ch', 
            'data', 
            'vagas', 
            'area',
            'publicos'
            ]