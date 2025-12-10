"""
URL configuration for CO2_PROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include  # Incluindo 'include'

# Removido: from django.urls.conf import include (Já está na linha acima)
# Removido: qualquer importação de 'views'

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Rota correta: Usa include() para apontar para o app 'usuario'
    path('', include('usuario.urls')),
    
    # Autenticação pronta do Django
    path('accounts/', include('django.contrib.auth.urls')),
]