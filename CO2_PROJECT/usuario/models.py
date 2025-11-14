from django.db import models

# Modelo de exemplo para armazenar contatos/pessoas (adaptável ao tema CO2)
class Pessoa(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100, help_text='Entre o nome')
	idade = models.IntegerField(help_text='Entre a idade', null=True, blank=True)
	salario = models.DecimalField(help_text='Entre o salário', decimal_places=2, max_digits=10, null=True, blank=True)
	email = models.EmailField(help_text='Informe o email', max_length=254, null=True, blank=True)
	dtNasc = models.DateField(help_text='Nascimento no formato YYYY-MM-DD', verbose_name='Data de nascimento', null=True, blank=True)

	def __str__(self):
		return f"{self.nome}"
