from django.contrib import admin
from django.urls import path
from usuario import views  # Importando as views que você acabou de criar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Rota da Página Inicial
    path('calculadora/', views.calculadora, name='calculadora'),
    path('usuario/', include('usuario.urls')), # Rota da Calculadora
    path('', include('usuario.urls')),
]