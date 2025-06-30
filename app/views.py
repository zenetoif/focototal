# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Dica, Cronograma
from .forms import CronogramaForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class IndexView(View):
    def get(self, request):
        dicas = Dica.objects.all()
        return render(request, 'index.html', {'dicas': dicas})

@method_decorator(login_required, name='dispatch')
class PomodoroView(View):
    def get(self, request):
        return render(request, 'pomodoro.html')

@method_decorator(login_required, name='dispatch')
class CronogramaView(View):
    def get(self, request):
        cronogramas = Cronograma.objects.filter(pessoa=request.user.pessoa)
        return render(request, 'cronograma.html', {'cronogramas': cronogramas})

@method_decorator(login_required, name='dispatch')
class CriarCronogramaView(View):
    def get(self, request):
        form = CronogramaForm()
        return render(request, 'criar_cronograma.html', {'form': form})

    def post(self, request):
        form = CronogramaForm(request.POST)
        if form.is_valid():
            cronograma = form.save(commit=False)
            cronograma.pessoa = request.user.pessoa
            cronograma.save()
            return redirect('cronograma')
        return render(request, 'criar_cronograma.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


