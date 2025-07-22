from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView,
    DashboardView, PomodoroView,
    CronogramaView, CriarCronogramaView,
    RecompensasView,
    IndexView,
    CentralEstudosView,  # NOVO IMPORT
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('cronograma/', CronogramaView.as_view(), name='cronograma'),
    path('cronograma/criar/', CriarCronogramaView.as_view(), name='criar_cronograma'),
    path('pomodoro/', PomodoroView.as_view(), name='pomodoro'),
    path('recompensas/', RecompensasView.as_view(), name='recompensas'),
    path('estudo/', CentralEstudosView.as_view(), name='estudo_dashboard'),  # NOVA ROTA
]
