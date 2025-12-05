from django.contrib import admin
from .models import RegistroCalculo # <-- Importa o modelo correto

# Registra o novo modelo no painel de administração
admin.site.register(RegistroCalculo)