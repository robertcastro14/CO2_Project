from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class RegistroCalculo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_calculo = models.DateTimeField(default=timezone.now)
    distancia = models.FloatField(verbose_name="Distância (km)")
    transporte = models.CharField(max_length=50, verbose_name="Meio de Transporte")
    co2_emitido = models.FloatField(verbose_name="CO2 Emitido (kg)")
    arvores = models.FloatField(verbose_name="Árvores para compensar")
    
    # --- ESTE CAMPO É OBRIGATÓRIO PARA O ERRO SUMIR ---
    custo_estimado = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="Custo Estimado (R$)"
    )
    # --------------------------------------------------

    def __str__(self):
        return f"{self.usuario.username} - {self.transporte} - {self.data_calculo}"

class DicaDeSustentabilidade(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Dica de Sustentabilidade"
        verbose_name_plural = "Dicas de Sustentabilidade"

class Notificacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dica = models.ForeignKey(DicaDeSustentabilidade, on_delete=models.CASCADE)
    lida = models.BooleanField(default=False)
    data_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notificação para {self.usuario.username}: {self.dica.titulo}"

    class Meta:
        ordering = ['-data_envio']
