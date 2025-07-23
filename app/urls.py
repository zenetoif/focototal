from django.urls import path
from .views import (
    IndexView, CustomLoginView, CustomLogoutView, CustomSignUpView,
    DashboardView, PomodoroView, CronogramaView, CriarCronogramaView,
    RecompensasView, resgatar_recompensa, CentralEstudosView,
    EditarCronogramaView, DeletarCronogramaView, ToggleCronogramaConclusaoView,
    CriarDicaView, CriarMaterialView,
)

urlpatterns = [
    path('', CustomLoginView.as_view(), name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignUpView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('cronograma/', CronogramaView.as_view(), name='cronograma'),
    path('criar_cronograma/', CriarCronogramaView.as_view(), name='criar_cronograma'),
    path('editar_cronograma/<int:cronograma_id>/', EditarCronogramaView.as_view(), name='editar_cronograma'),
    path('deletar_cronograma/<int:cronograma_id>/', DeletarCronogramaView.as_view(), name='deletar_cronograma'),
    path('toggle_cronograma/<int:cronograma_id>/', ToggleCronogramaConclusaoView.as_view(), name='toggle_cronograma'),
    path('pomodoro/', PomodoroView.as_view(), name='pomodoro'),
    path('recompensas/', RecompensasView.as_view(), name='recompensas'),
    path('resgatar-recompensa/', resgatar_recompensa, name='resgatar_recompensa'),
    path('estudo/', CentralEstudosView.as_view(), name='estudo_dashboard'),
    path('criar_dica/', CriarDicaView.as_view(), name='criar_dica'),
    path('criar_material/', CriarMaterialView.as_view(), name='criar_material'),
]
