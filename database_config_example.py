# Exemplo de configuração para config/settings.py
# Copie e modifique conforme necessário

# ==============================================
# CONFIGURAÇÃO POSTGRESQL (RECOMENDADO)
# ==============================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'focototal2025h',          # Nome do banco
        'USER': 'postgres',                # Usuário do PostgreSQL
        'PASSWORD': '123456',              # Senha do PostgreSQL
        'HOST': 'localhost',               # Host do banco
        'PORT': '5432',                    # Porta do PostgreSQL
    }
}

# ==============================================
# CONFIGURAÇÃO SQLITE (PARA DESENVOLVIMENTO)
# ==============================================

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# ==============================================
# OUTRAS CONFIGURAÇÕES IMPORTANTES
# ==============================================

# Para produção, sempre definir:
# DEBUG = False
# ALLOWED_HOSTS = ['seu-dominio.com', 'www.seu-dominio.com']

# Para desenvolvimento local:
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Chave secreta (gere uma nova para produção)
# SECRET_KEY = 'sua-chave-secreta-super-segura-aqui'
