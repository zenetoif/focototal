from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, PomodoroView, CronogramaView, CriarCronogramaView,
    CustomLoginView, CustomLogoutView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pomodoro/', PomodoroView.as_view(), name='pomodoro'),
    path('cronograma/', CronogramaView.as_view(), name='cronograma'),
    path('cronograma/criar/', CriarCronogramaView.as_view(), name='criar_cronograma'),
    path('login/', CustomLoginView.as_view(), name='login'),  # ESSA LINHA
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
