# 🚀 GUIA RÁPIDO - FOCO TOTAL

## ⚡ Instalação Express (5 minutos)

### 1. Clone o repositório
```bash
git clone https://github.com/zenetoif/focototal.git
cd focototal
```

### 2. Execute o script de instalação

**Windows:**
```cmd
setup_windows.bat
```

**Linux/Mac:**
```bash
chmod +x setup_linux_mac.sh
./setup_linux_mac.sh
```

### 3. Configure o banco de dados
- Abra `config/settings.py`
- Configure PostgreSQL (recomendado) ou use SQLite
- Veja exemplos em `database_config_example.py`

### 4. Finalize a configuração
```bash
# Ative o ambiente virtual (se não estiver ativo)
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Crie um superusuário
python manage.py createsuperuser

# (Opcional) Popule com dados de exemplo
python manage.py shell < popular_dados.py

# Execute o servidor
python manage.py runserver
```

### 5. Acesse a aplicação
- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 🔧 Configuração PostgreSQL

### Instalar PostgreSQL
- **Windows**: https://www.postgresql.org/download/windows/
- **Linux**: `sudo apt install postgresql postgresql-contrib`
- **Mac**: `brew install postgresql`

### Criar banco de dados
```sql
-- Entre no psql como postgres
CREATE DATABASE focototal2025h;
CREATE USER focototal WITH PASSWORD 'suasenha123';
GRANT ALL PRIVILEGES ON DATABASE focototal2025h TO focototal;
```

### Configurar em settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'focototal2025h',
        'USER': 'focototal',
        'PASSWORD': 'suasenha123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📱 Primeiros Passos no Sistema

1. **Cadastre-se** ou faça login
2. **Explore o Dashboard** - visão geral de tudo
3. **Crie um Cronograma** - organize seus estudos
4. **Use o Pomodoro** - técnica de foco de 25min
5. **Ganhe Pontos** - sistema de gamificação
6. **Troque por Recompensas** - motive-se a estudar
7. **Acesse a Central de Estudos** - dicas e materiais

---

## 🆘 Problemas Comuns

### "ModuleNotFoundError: No module named 'psycopg2'"
```bash
pip install psycopg2-binary
```

### Erro de migração
```bash
python manage.py makemigrations --empty app
python manage.py migrate --fake-initial
```

### Problema com perfil de usuário
```bash
python manage.py fix_user_integrity
```

### Django não encontrado
```bash
# Certifique-se que o ambiente virtual está ativo
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install Django
```

---

## 📞 Ajuda

- 📖 **README completo**: Veja README.md
- 🐛 **Bugs**: Abra uma issue no GitHub
- ❓ **Dúvidas**: Consulte a documentação do Django

**Bons estudos! 🎯📚**
