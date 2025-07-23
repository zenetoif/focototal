from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Pessoa

@receiver(post_save, sender=User)
def criar_pessoa_automaticamente(sender, instance, created, **kwargs):
    if created:
        # Criar perfil Pessoa com nome padrão (será atualizado pelo formulário se necessário)
        nome_default = instance.get_full_name() or instance.username
        Pessoa.objects.get_or_create(
            user=instance,
            defaults={'nome_completo': nome_default}
        )
