from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cronograma, Dica, MaterialApoio, Pessoa

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = ['titulo', 'descricao', 'data', 'hora_inicio', 'hora_fim', 'publico']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Estudos de Matemática'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva os tópicos ou detalhes do cronograma'
            }),
            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'hora_inicio': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'hora_fim': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'publico': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'titulo': 'Título do Cronograma',
            'descricao': 'Descrição (opcional)',
            'data': 'Data',
            'hora_inicio': 'Hora de Início',
            'hora_fim': 'Hora de Fim',
            'publico': 'Tornar cronograma público',
        }


class DicaForm(forms.ModelForm):
    class Meta:
        model = Dica
        fields = ['titulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Como manter o foco durante os estudos'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreva a dica de estudo em detalhes...'
            }),
        }
        labels = {
            'titulo': 'Título da Dica',
            'conteudo': 'Conteúdo da Dica',
        }


class MaterialApoioForm(forms.ModelForm):
    class Meta:
        model = MaterialApoio
        fields = ['titulo', 'descricao', 'link', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Curso de Python para Iniciantes'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descreva o material de apoio...'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemplo.com/material'
            }),
            'imagem': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemplo.com/imagem.jpg (opcional)'
            }),
        }
        labels = {
            'titulo': 'Título do Material',
            'descricao': 'Descrição',
            'link': 'Link do Material',
            'imagem': 'URL da Imagem (opcional)',
        }


class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome completo'
        }),
        label='Nome Completo'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        }),
        label='E-mail'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'nome_completo', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite seu nome de usuário'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })
        self.fields['username'].label = 'Nome de Usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de Senha'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # O signal criará automaticamente o perfil Pessoa,
            # então só precisamos atualizar o nome_completo depois
            pessoa, created = Pessoa.objects.get_or_create(
                user=user,
                defaults={'nome_completo': self.cleaned_data['nome_completo']}
            )
            if not created:
                pessoa.nome_completo = self.cleaned_data['nome_completo']
                pessoa.save()
        return user
