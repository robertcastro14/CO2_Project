from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('historico/', views.historico, name='historico'),
    # NOVO: URL para marcar a notificação como lida
    path('notificacao/<int:notificacao_id>/lida/', views.marcar_notificacao_lida, name='marcar_notificacao_lida'),
]