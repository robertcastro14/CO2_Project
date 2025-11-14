from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Pessoa


class ContatoListView(View):
	def get(self, request, *args, **kwargs):
		pessoas = Pessoa.objects.all()
		contexto = { 'pessoas': pessoas }
		return render(request, 'usuario/listaContatos.html', contexto)


def buscaUmContato(request):
	return render(request, 'usuario/buscaUmContato.html')


def respostaBuscaUmContato(request):
	nome = request.GET.get('nome', '')
	pessoas = Pessoa.objects.all().filter(nome__icontains=nome)
	contexto = { 'pessoas': pessoas }
	return render(request, 'usuario/listaContatos.html', contexto)
