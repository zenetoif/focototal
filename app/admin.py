# app/admin.py
from django.contrib import admin
from .models import Pessoa, Cronograma, SessaoPomodoro, Dica

admin.site.register(Pessoa)
admin.site.register(Cronograma)
admin.site.register(SessaoPomodoro)
admin.site.register(Dica)
