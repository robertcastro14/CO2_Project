from django.urls import path
from . import views

urlpatterns = [
    # ... suas rotas existentes
    path('', views.home, name='home'),
    path('calculadora/', views.calculadora, name='calculadora'),
    
    # Rota para o histórico
    path('historico/', views.historico, name='historico'), 
]