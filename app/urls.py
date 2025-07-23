from django.urls import path
from .views import (
    IndexView, CustomLoginView, CustomLogoutView,
    DashboardView, PomodoroView, CronogramaView, CriarCronogramaView,
    RecompensasView, resgatar_recompensa, CentralEstudosView,
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
    path('resgatar-recompensa/', resgatar_recompensa, name='resgatar_recompensa'),
    path('estudo/', CentralEstudosView.as_view(), name='estudo_dashboard'),
]
