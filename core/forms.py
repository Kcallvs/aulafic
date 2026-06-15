from django import forms
from .models import Area, PublicoAlvo, Curso

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