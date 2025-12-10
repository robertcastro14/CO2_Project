from django.urls import path
from . import views  # Importante: essa linha carrega as views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('historico/', views.historico, name='historico'),
    path('notificacao/<int:notificacao_id>/lida/', views.marcar_notificacao_lida, name='marcar_notificacao_lida'),
    
    # Adicione as rotas aqui, onde 'views' foi importado
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]