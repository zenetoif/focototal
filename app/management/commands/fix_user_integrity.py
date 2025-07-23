from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Pessoa

class Command(BaseCommand):
    help = 'Corrige problemas de integridade entre User e Pessoa'

    def handle(self, *args, **options):
        self.stdout.write("Verificando integridade User <-> Pessoa...")
        
        # Verificar usuários sem perfil Pessoa
        users_sem_pessoa = User.objects.filter(pessoa__isnull=True)
        if users_sem_pessoa.exists():
            self.stdout.write(f"Encontrados {users_sem_pessoa.count()} usuários sem perfil Pessoa")
            for user in users_sem_pessoa:
                nome = user.get_full_name() or user.username
                Pessoa.objects.create(user=user, nome_completo=nome)
                self.stdout.write(f"Criado perfil para: {user.username}")
        
        # Verificar perfis Pessoa sem usuário (não deveria acontecer por causa do CASCADE)
        pessoas_sem_user = Pessoa.objects.filter(user__isnull=True)
        if pessoas_sem_user.exists():
            self.stdout.write(f"Encontrados {pessoas_sem_user.count()} perfis Pessoa órfãos")
            pessoas_sem_user.delete()
            self.stdout.write("Perfis órfãos removidos")
        
        # Estatísticas finais
        total_users = User.objects.count()
        total_pessoas = Pessoa.objects.count()
        
        self.stdout.write(f"\nEstatísticas finais:")
        self.stdout.write(f"Total de usuários: {total_users}")
        self.stdout.write(f"Total de perfis Pessoa: {total_pessoas}")
        
        if total_users == total_pessoas:
            self.stdout.write(self.style.SUCCESS("✓ Integridade verificada: todos os usuários têm perfil Pessoa"))
        else:
            self.stdout.write(self.style.ERROR(f"✗ Problema: {total_users} usuários != {total_pessoas} perfis"))
