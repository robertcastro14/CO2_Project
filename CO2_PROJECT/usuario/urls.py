from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='lista-contatos'),
    path('busca/', views.buscaUmContato, name='busca-contato'),
    path('retorno-busca/', views.respostaBuscaUmContato, name='mostra-contato'),
]
