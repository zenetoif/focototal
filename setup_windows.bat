@echo off
echo =========================================
echo     FOCO TOTAL - SCRIPT DE INSTALACAO
echo =========================================
echo.

echo [1/7] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado! Instale Python 3.8+ e tente novamente.
    pause
    exit /b 1
)

echo.
echo [2/7] Criando ambiente virtual...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERRO: Falha ao criar ambiente virtual!
    pause
    exit /b 1
)

echo.
echo [3/7] Ativando ambiente virtual...
call venv\Scripts\activate

echo.
echo [4/7] Atualizando pip...
python -m pip install --upgrade pip

echo.
echo [5/7] Instalando dependencias...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERRO: Falha ao instalar dependencias!
    pause
    exit /b 1
)

echo.
echo [6/7] Executando migracoes...
python manage.py makemigrations
python manage.py migrate
if %errorlevel% neq 0 (
    echo AVISO: Problemas com migracoes. Configure o banco de dados primeiro.
)

echo.
echo [7/7] Verificando projeto...
python manage.py check

echo.
echo =========================================
echo        INSTALACAO CONCLUIDA!
echo =========================================
echo.
echo Proximo passo:
echo 1. Configure o banco de dados em config/settings.py
echo 2. Execute: python manage.py createsuperuser
echo 3. Execute: python manage.py runserver
echo 4. Acesse: http://127.0.0.1:8000/
echo.
echo Para ativar o ambiente virtual novamente:
echo   venv\Scripts\activate
echo.
pause
