# Teste de cadastro de usuário
# Execute: python manage.py shell < test_signup.py

from django.contrib.auth.models import User
from app.models import Pessoa
from app.forms import CustomUserCreationForm

print("=== Teste de Cadastro ===")

# Dados de teste
test_data = {
    'nome_completo': 'Usuário Teste',
    'username': 'usuarioteste',
    'email': 'teste@exemplo.com',
    'password1': 'senha123456',
    'password2': 'senha123456'
}

# Verificar se usuário já existe
if User.objects.filter(username=test_data['username']).exists():
    print("Usuário de teste já existe, removendo...")
    User.objects.filter(username=test_data['username']).delete()

# Testar formulário
form = CustomUserCreationForm(data=test_data)
if form.is_valid():
    try:
        user = form.save()
        print(f"✓ Usuário criado: {user.username}")
        print(f"✓ Email: {user.email}")
        
        # Verificar se perfil Pessoa foi criado
        try:
            pessoa = user.pessoa
            print(f"✓ Perfil Pessoa criado: {pessoa.nome_completo}")
            print(f"✓ Pontos iniciais: {pessoa.pontos}")
        except Pessoa.DoesNotExist:
            print("✗ Erro: perfil Pessoa não foi criado")
            
    except Exception as e:
        print(f"✗ Erro ao salvar: {e}")
else:
    print("✗ Formulário inválido:")
    for field, errors in form.errors.items():
        print(f"  {field}: {errors}")

print("\n=== Estatísticas Finais ===")
print(f"Total de usuários: {User.objects.count()}")
print(f"Total de perfis Pessoa: {Pessoa.objects.count()}")
