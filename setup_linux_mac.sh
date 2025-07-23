#!/bin/bash

echo "========================================="
echo "     FOCO TOTAL - SCRIPT DE INSTALACAO"
echo "========================================="
echo

echo "[1/7] Verificando Python..."
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "ERRO: Python não encontrado! Instale Python 3.8+ e tente novamente."
    exit 1
fi

# Detectar comando Python correto
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PIP_CMD="pip3"
else
    PYTHON_CMD="python"
    PIP_CMD="pip"
fi

$PYTHON_CMD --version

echo
echo "[2/7] Criando ambiente virtual..."
$PYTHON_CMD -m venv venv
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao criar ambiente virtual!"
    exit 1
fi

echo
echo "[3/7] Ativando ambiente virtual..."
source venv/bin/activate

echo
echo "[4/7] Atualizando pip..."
$PYTHON_CMD -m pip install --upgrade pip

echo
echo "[5/7] Instalando dependências..."
$PIP_CMD install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERRO: Falha ao instalar dependências!"
    exit 1
fi

echo
echo "[6/7] Executando migrações..."
$PYTHON_CMD manage.py makemigrations
$PYTHON_CMD manage.py migrate
if [ $? -ne 0 ]; then
    echo "AVISO: Problemas com migrações. Configure o banco de dados primeiro."
fi

echo
echo "[7/7] Verificando projeto..."
$PYTHON_CMD manage.py check

echo
echo "========================================="
echo "        INSTALAÇÃO CONCLUÍDA!"
echo "========================================="
echo
echo "Próximo passo:"
echo "1. Configure o banco de dados em config/settings.py"
echo "2. Execute: $PYTHON_CMD manage.py createsuperuser"
echo "3. Execute: $PYTHON_CMD manage.py runserver"
echo "4. Acesse: http://127.0.0.1:8000/"
echo
echo "Para ativar o ambiente virtual novamente:"
echo "   source venv/bin/activate"
echo
