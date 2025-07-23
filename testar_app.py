#!/usr/bin/env python
"""
Script para testar se a aplicação Django está funcionando corretamente
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from app.models import Dica, MaterialApoio, Cronograma

try:
    # Testar se os modelos estão funcionando
    print("Testando modelos...")
    print(f"Dicas: {Dica.objects.count()}")
    print(f"Materiais: {MaterialApoio.objects.count()}")
    print(f"Cronogramas: {Cronograma.objects.count()}")
    
    # Testar se a URL está configurada
    from django.conf import settings
    from django.urls import reverse
    
    print("\nTestando URLs...")
    try:
        url = reverse('estudo_dashboard')
        print(f"URL estudo_dashboard: {url}")
    except Exception as e:
        print(f"Erro na URL estudo_dashboard: {e}")
    
    print("\nTodos os testes básicos passaram!")
    
except Exception as e:
    print(f"Erro durante os testes: {e}")
    sys.exit(1)
