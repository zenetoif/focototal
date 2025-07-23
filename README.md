# 🎯 Foco Total

**Aplicação Web para Apoio à Concentração nos Estudos**

Uma plataforma completa desenvolvida em Django para ajudar estudantes a organizarem seus estudos, gerenciarem cronogramas, utilizarem a técnica Pomodoro e acompanharem seu progresso através de um sistema de gamificação.

![Foco Total](https://img.shields.io/badge/Django-4.2+-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

## 📋 Funcionalidades

### 🎨 **Interface Unificada**
- **Glass Morphism Design**: Interface moderna com efeitos de vidro translúcido
- **Tema Escuro**: Gradientes elegantes que reduzem cansaço visual
- **Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- **Navegação Intuitiva**: Menu consistente em todas as páginas

### 🔐 **Sistema de Autenticação**
- **Cadastro de Usuários**: Registro completo com nome, email e senha
- **Login Seguro**: Autenticação integrada do Django
- **Perfis Automáticos**: Criação automática de perfil personalizado
- **Redirecionamento Inteligente**: Usuários logados vão direto ao dashboard

### 📅 **Gerenciamento de Cronogramas**
- **Criação de Cronogramas**: Organize seus estudos por data, hora e matéria
- **Cronogramas Públicos**: Compartilhe seus cronogramas com a comunidade
- **Edição e Exclusão**: Gerencie seus cronogramas facilmente
- **Filtros Avançados**: Busque por data, título ou status
- **Status de Conclusão**: Marque cronogramas como concluídos

### ⏱️ **Timer Pomodoro**
- **Técnica Pomodoro**: Timer de 25 minutos com pausas de 5 minutos
- **Interface Visual**: Design atrativo com controles intuitivos
- **Histórico de Sessões**: Acompanhe suas sessões de estudo
- **Integração com Pontos**: Ganhe pontos por cada sessão completada

### 🏆 **Sistema de Gamificação**
- **Pontos por Atividade**: Ganhe pontos ao completar cronogramas e sessões Pomodoro
- **Sistema de Recompensas**: Troque pontos por recompensas personalizadas
- **Acompanhamento de Progresso**: Visualize seu desenvolvimento
- **Motivação Contínua**: Sistema que incentiva o estudo regular

### 📚 **Central de Estudos**
- **Dicas de Estudo**: Compartilhe e descubra técnicas de estudo eficazes
- **Material de Apoio**: Links para recursos educacionais externos
- **Comunidade**: Acesse conteúdo compartilhado por outros usuários
- **Gestão de Conteúdo**: Adicione suas próprias dicas e materiais

### 📊 **Dashboard Personalizado**
- **Visão Geral**: Acesso rápido a todas as funcionalidades
- **Estatísticas**: Acompanhe seu progresso e pontuação
- **Links Diretos**: Navegação rápida para todas as seções
- **Interface Unificada**: Design consistente em toda a aplicação

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 4.2+**: Framework web robusto e seguro
- **Python 3.8+**: Linguagem de programação principal
- **PostgreSQL**: Banco de dados relacional confiável
- **Django Signals**: Automação de tarefas internas

### Frontend
- **HTML5 & CSS3**: Markup e estilos modernos
- **Bootstrap 5.3**: Framework CSS responsivo
- **JavaScript**: Interatividade e funcionalidades dinâmicas
- **Font Awesome**: Ícones profissionais
- **Google Fonts (Outfit)**: Tipografia moderna

### Design
- **Glass Morphism**: Efeitos de vidro translúcido
- **Gradientes Personalizados**: Paleta de cores harmoniosa
- **Animações CSS**: Transições suaves e elegantes
- **Layout Responsivo**: Adaptável a qualquer tamanho de tela

## 🚀 Como Rodar o Projeto

### Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8 ou superior**
- **PostgreSQL 13 ou superior**
- **Git** (para clonar o repositório)
- **pip** (gerenciador de pacotes do Python)

### 📥 1. Clonando o Repositório

```bash
# Clone o repositório
git clone https://github.com/zenetoif/focototal.git

# Entre no diretório do projeto
cd focototal
```

### 🐍 2. Configurando o Ambiente Virtual

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\\Scripts\\activate
# No Linux/Mac:
source venv/bin/activate
```

### 📦 3. Instalando Dependências

```bash
# Instale as dependências do projeto
pip install -r requirements.txt
```

### 🗄️ 4. Configurando o Banco de Dados

#### PostgreSQL
1. **Instale o PostgreSQL** se ainda não tiver instalado
2. **Crie um banco de dados**:
   ```sql
   CREATE DATABASE focototal2025h;
   CREATE USER postgres WITH PASSWORD '123456';
   GRANT ALL PRIVILEGES ON DATABASE focototal2025h TO postgres;
   ```

3. **Configure as credenciais** em `config/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'focototal2025h',
           'USER': 'postgres',
           'PASSWORD': '123456',  # Altere para sua senha
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

#### SQLite (Alternativa mais simples)
Se preferir usar SQLite para desenvolvimento, altere em `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 🔧 5. Configurando o Django

```bash
# Execute as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário (admin)
python manage.py createsuperuser

# (Opcional) Popule o banco com dados de exemplo
python manage.py shell < popular_dados.py

# (Opcional) Verifique a integridade dos dados
python manage.py fix_user_integrity
```

### ▶️ 6. Executando o Servidor

```bash
# Inicie o servidor de desenvolvimento
python manage.py runserver

# O servidor estará disponível em: http://127.0.0.1:8000/
```

### 🌐 7. Acessando a Aplicação

1. **Página Inicial**: http://127.0.0.1:8000/
2. **Login**: http://127.0.0.1:8000/login/
3. **Cadastro**: http://127.0.0.1:8000/signup/
4. **Admin Django**: http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto

```
focototal/
├── app/                          # Aplicação principal
│   ├── __init__.py
│   ├── admin.py                  # Configuração do admin
│   ├── apps.py                   # Configuração da app
│   ├── forms.py                  # Formulários personalizados
│   ├── models.py                 # Modelos do banco de dados
│   ├── signals.py                # Signals automáticos
│   ├── urls.py                   # URLs da aplicação
│   ├── views.py                  # Views e lógica de negócio
│   ├── migrations/               # Migrações do banco de dados
│   ├── management/               # Comandos personalizados
│   │   └── commands/
│   │       └── fix_user_integrity.py
│   ├── static/                   # Arquivos estáticos
│   │   └── img/                  # Imagens do projeto
│   └── templates/                # Templates HTML
│       ├── base.html             # Template base
│       ├── dashboard.html        # Dashboard principal
│       ├── cronograma.html       # Gerenciamento de cronogramas
│       ├── pomodoro.html         # Timer Pomodoro
│       ├── recompensas.html      # Sistema de recompensas
│       ├── estudo_dashboard.html # Central de estudos
│       └── registration/         # Templates de autenticação
│           ├── login.html        # Página de login
│           └── signup.html       # Página de cadastro
├── config/                       # Configurações do Django
│   ├── __init__.py
│   ├── settings.py               # Configurações principais
│   ├── urls.py                   # URLs raiz do projeto
│   ├── wsgi.py                   # WSGI para deploy
│   └── asgi.py                   # ASGI para deploy
├── manage.py                     # Script de gerenciamento Django
├── requirements.txt              # Dependências do projeto
├── popular_dados.py              # Script para dados de exemplo
├── test_signup.py                # Script de teste de cadastro
└── README.md                     # Documentação do projeto
```

## 💾 Modelos de Dados

### 👤 Pessoa
- Perfil do usuário com pontos de gamificação
- Relacionamento um-para-um com User do Django

### 📅 Cronograma
- Cronogramas de estudo com data, hora e status
- Podem ser públicos ou privados
- Status de conclusão

### 🏆 Recompensa
- Sistema de recompensas baseado em pontos
- Custam pontos para serem resgatadas

### ⏱️ SessaoPomodoro
- Registro de sessões de estudo Pomodoro
- Histórico de produtividade

### 💡 Dica
- Dicas de estudo compartilhadas pela comunidade

### 📚 MaterialApoio
- Links para materiais educacionais externos
- Recursos de apoio ao estudo

## 🔧 Comandos Úteis

```bash
# Verificar integridade do projeto
python manage.py check

# Criar novas migrações após alterar models
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos (para produção)
python manage.py collectstatic

# Executar shell interativo do Django
python manage.py shell

# Verificar integridade dos perfis de usuário
python manage.py fix_user_integrity

# Executar testes
python manage.py test
```

## 🚀 Deploy em Produção

### Preparação para Deploy
1. **Configure as variáveis de ambiente**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['seu-dominio.com']
   ```

2. **Configure banco de dados de produção**
3. **Configure arquivos estáticos**:
   ```bash
   python manage.py collectstatic
   ```

4. **Configure servidor web** (Nginx, Apache)
5. **Configure WSGI** (Gunicorn, uWSGI)

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é desenvolvido como parte do curso no IFSULDEMINAS - Campus Muzambinho.

## 🆘 Solução de Problemas

### Erro de Banco de Dados
Se você encontrar erros relacionados ao PostgreSQL:
1. Verifique se o PostgreSQL está rodando
2. Confirme as credenciais em `settings.py`
3. Tente usar SQLite como alternativa

### Erro de Dependências
Se houver problemas com as dependências:
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Erro de Migrações
Se as migrações falharem:
```bash
python manage.py makemigrations --empty app
python manage.py migrate --fake-initial
```

### Erro de Integridade de Usuário
Se houver problemas com perfis de usuário:
```bash
python manage.py fix_user_integrity
```

## 📞 Suporte

Para dúvidas ou problemas:
- Verifique a documentação do Django: https://docs.djangoproject.com/
- Consulte os logs do servidor para mensagens de erro específicas
- Execute `python manage.py check` para verificar problemas de configuração

---

**Desenvolvido com ❤️ para IFSULDEMINAS - Campus Muzambinho**

*Foco Total - Transformando estudos em conquistas!* 🎯
