from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Dica, Cronograma, MaterialApoio, Pessoa, Recompensa
from .forms import CronogramaForm


class IndexView(View):
    def get(self, request):
        return render(request, 'login_index.html')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class PomodoroView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'pomodoro.html')


class CronogramaView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return redirect('index')

        cronogramas = Cronograma.objects.filter(pessoa=pessoa)

        # Filtros do formulário GET
        data = request.GET.get('data')
        titulo = request.GET.get('titulo')

        if data:
            cronogramas = cronogramas.filter(data=data)
        if titulo:
            cronogramas = cronogramas.filter(titulo__icontains=titulo)

        return render(request, 'cronograma.html', {'cronogramas': cronogramas})


class CriarCronogramaView(LoginRequiredMixin, View):
    def get(self, request):
        form = CronogramaForm()
        return render(request, 'criar_cronograma.html', {'form': form})

    def post(self, request):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return redirect('index')

        form = CronogramaForm(request.POST)
        if form.is_valid():
            cronograma = form.save(commit=False)
            cronograma.pessoa = pessoa
            cronograma.save()
            return redirect('cronograma')
        return render(request, 'criar_cronograma.html', {'form': form})


class RecompensasView(LoginRequiredMixin, ListView):
    model = Recompensa
    template_name = 'recompensas.html'
    context_object_name = 'recompensas'

    def get_queryset(self):
        try:
            pessoa = self.request.user.pessoa
            return Recompensa.objects.filter(pessoa=pessoa)
        except ObjectDoesNotExist:
            return Recompensa.objects.none()


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class CentralEstudosView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return redirect('index')

        dicas = Dica.objects.all()
        materiais = MaterialApoio.objects.all()
        cronogramas = Cronograma.objects.filter(publico=True)

        context = {
            'dicas': dicas,
            'materiais': materiais,
            'cronogramas': cronogramas,
        }
        return render(request, 'estudo_dashboard.html', context)
