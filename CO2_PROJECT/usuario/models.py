from django.db import models
from django.contrib.auth.models import User

class RegistroCalculo(models.Model):
    # Relaciona o cálculo ao usuário que o fez
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Dados do cálculo
    distancia = models.FloatField(verbose_name="Distância (km)")
    transporte = models.CharField(max_length=50, verbose_name="Meio de Transporte")
    
    # Resultados
    co2_emitido = models.FloatField(verbose_name="CO2 Emitido (kg)")
    arvores = models.FloatField(verbose_name="Árvores para compensar")
    
    # Data automática (guarda o momento exato do cálculo)
    data_calculo = models.DateTimeField(auto_now_add=True, verbose_name="Data do Cálculo")

    def __str__(self):
        return f"{self.usuario.username} - {self.transporte} - {self.co2_emitido}kg"