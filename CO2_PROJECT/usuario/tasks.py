from celery import shared_task
from django.contrib.auth.models import User
from .models import DicaDeSustentabilidade, Notificacao
import random

@shared_task
def enviar_dica_diaria():
    """
    Tarefa agendada: Seleciona uma dica aleatória e notifica todos os usuários ativos.
    """
    try:
        # 1. Obter uma dica ativa aleatória
        dicas_ativas = list(DicaDeSustentabilidade.objects.filter(ativa=True))
        
        if not dicas_ativas:
            return "Nenhuma dica ativa encontrada."
            
        dica_selecionada = random.choice(dicas_ativas)
        
        # 2. Obter todos os IDs de usuários ativos
        usuarios_ids = User.objects.filter(is_active=True).values_list('id', flat=True)
        
        # 3. Criar as notificações em massa (bulk_create é mais eficiente)
        novas_notificacoes = [
            Notificacao(usuario_id=user_id, dica=dica_selecionada, lida=False)
            for user_id in usuarios_ids
        ]
            
        Notificacao.objects.bulk_create(novas_notificacoes)
        
        return f"Dica '{dica_selecionada.titulo}' enviada para {len(novas_notificacoes)} usuários."

    except Exception as e:
        return f"Erro ao enviar dica diária: {e}"