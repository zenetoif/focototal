import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError

from .models import Recompensa, Pessoa, Cronograma, Dica, MaterialApoio
from .forms import CronogramaForm, DicaForm, MaterialApoioForm, CustomUserCreationForm


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


@method_decorator(login_required, name='dispatch')
@csrf_exempt
def resgatar_recompensa(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            recompensa_id = data.get('recompensa_id')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'success': False, 'message': 'Dados inválidos.'})

        try:
            recompensa = Recompensa.objects.get(id=recompensa_id, pessoa=request.user.pessoa)
            pessoa = request.user.pessoa
        except Recompensa.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Recompensa não encontrada.'})

        custo = recompensa.pontos_custo

        if pessoa.pontos < custo:
            return JsonResponse({'success': False, 'message': 'Você não tem pontos suficientes para resgatar.'})

        pessoa.pontos -= custo
        pessoa.save()

        recompensa.resgatada = True
        recompensa.save()

        return JsonResponse({'success': True, 'message': 'Recompensa resgatada com sucesso!', 'pontos_atualizados': pessoa.pontos})

    return JsonResponse({'success': False, 'message': 'Método inválido.'})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def form_invalid(self, form):
        """Adiciona contexto para formulário inválido"""
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class CustomSignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Conta criada com sucesso! Bem-vindo ao Foco Total!')
                return redirect('dashboard')
            except IntegrityError as e:
                # Se houver erro de integridade, tentar recuperar
                if 'app_pessoa_user_id_key' in str(e):
                    messages.error(request, 'Erro interno: perfil de usuário já existe. Tente fazer login.')
                    return redirect('login')
                else:
                    messages.error(request, 'Erro ao criar conta. Tente novamente.')
        return render(request, 'registration/signup.html', {'form': form})


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


class EditarCronogramaView(LoginRequiredMixin, View):
    def get(self, request, cronograma_id):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return redirect('index')
        
        cronograma = get_object_or_404(Cronograma, id=cronograma_id, pessoa=pessoa)
        form = CronogramaForm(instance=cronograma)
        return render(request, 'editar_cronograma.html', {'form': form, 'cronograma': cronograma})

    def post(self, request, cronograma_id):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return redirect('index')
        
        cronograma = get_object_or_404(Cronograma, id=cronograma_id, pessoa=pessoa)
        form = CronogramaForm(request.POST, instance=cronograma)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Cronograma editado com sucesso!')
            return redirect('cronograma')
        
        return render(request, 'editar_cronograma.html', {'form': form, 'cronograma': cronograma})


class DeletarCronogramaView(LoginRequiredMixin, View):
    def post(self, request, cronograma_id):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return redirect('index')
        
        cronograma = get_object_or_404(Cronograma, id=cronograma_id, pessoa=pessoa)
        cronograma.delete()
        messages.success(request, 'Cronograma deletado com sucesso!')
        return redirect('cronograma')


class ToggleCronogramaConclusaoView(LoginRequiredMixin, View):
    def post(self, request, cronograma_id):
        try:
            pessoa = request.user.pessoa
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'message': 'Usuário não encontrado.'})
        
        cronograma = get_object_or_404(Cronograma, id=cronograma_id, pessoa=pessoa)
        cronograma.concluido = not cronograma.concluido
        cronograma.save()
        
        # Adicionar pontos quando marcar como concluído
        if cronograma.concluido:
            pessoa.pontos += 10  # 10 pontos por cronograma concluído
            pessoa.save()
            message = 'Cronograma marcado como concluído! +10 pontos!'
        else:
            message = 'Cronograma desmarcado como concluído.'
        
        return JsonResponse({
            'success': True, 
            'message': message,
            'concluido': cronograma.concluido,
            'pontos_atualizados': pessoa.pontos
        })


class CriarDicaView(LoginRequiredMixin, View):
    def get(self, request):
        form = DicaForm()
        return render(request, 'criar_dica.html', {'form': form})

    def post(self, request):
        form = DicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dica de estudo criada com sucesso!')
            return redirect('estudo_dashboard')
        return render(request, 'criar_dica.html', {'form': form})


class CriarMaterialView(LoginRequiredMixin, View):
    def get(self, request):
        form = MaterialApoioForm()
        return render(request, 'criar_material.html', {'form': form})

    def post(self, request):
        form = MaterialApoioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material de apoio criado com sucesso!')
            return redirect('estudo_dashboard')
        return render(request, 'criar_material.html', {'form': form})
