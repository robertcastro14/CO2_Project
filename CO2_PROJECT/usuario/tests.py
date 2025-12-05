from django.test import TestCase
from django.contrib.auth.models import User

from .models import DicaDeSustentabilidade, Notificacao
from .tasks import enviar_dica_diaria


class EnviarDicaTaskTest(TestCase):
	def test_enviar_dica_cria_notificacoes_para_usuarios_ativos(self):
		# criar usuários (2 ativos, 1 inativo)
		User.objects.create_user(username='active1', password='pw')
		User.objects.create_user(username='inactive', password='pw', is_active=False)
		User.objects.create_user(username='active2', password='pw')

		# criar uma dica ativa
		DicaDeSustentabilidade.objects.create(titulo='Teste', conteudo='Conteúdo', ativa=True)

		# executar a task diretamente (sincronamente)
		result = enviar_dica_diaria()

		# verificar que notificações foram criadas apenas para usuários ativos
		active_count = User.objects.filter(is_active=True).count()
		notif_count = Notificacao.objects.count()

		self.assertEqual(notif_count, active_count)
		self.assertIsInstance(result, str)
