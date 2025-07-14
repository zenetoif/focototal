from django.urls import path
from .views import (
    IndexView, PomodoroView, CronogramaView, CriarCronogramaView,
    CustomLoginView, CustomLogoutView
)

app_name = 'app'  # Útil para usar {% url 'app:index' %}, etc.

urlpatterns = [
    # Página inicial
    path('', IndexView.as_view(), name='index'),

    # Sessão Pomodoro
    path('pomodoro/', PomodoroView.as_view(), name='pomodoro'),

    # Cronograma
    path('cronograma/', CronogramaView.as_view(), name='cronograma'),
    path('cronograma/novo/', CriarCronogramaView.as_view(), name='criar_cronograma'),

    # Autenticação
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
