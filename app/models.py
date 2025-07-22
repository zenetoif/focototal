from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo


class Cronograma(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    publico = models.BooleanField(default=False)  # NOVO CAMPO

    def __str__(self):
        return f"{self.titulo} ({self.data})"


class Relatorio(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    total_pomodoros = models.IntegerField(default=0)
    tempo_total = models.IntegerField(help_text="Tempo total em minutos", default=0)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Relatório de {self.pessoa.nome_completo} em {self.data}"


class Recompensa(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_obtida = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class SessaoPomodoro(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    duracao = models.IntegerField(help_text="Duração em minutos")
    pausas = models.IntegerField()

    def __str__(self):
        return f"Pomodoro em {self.data} ({self.duracao} min)"


class Dica(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo


class MaterialApoio(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    link = models.URLField()
    imagem = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
