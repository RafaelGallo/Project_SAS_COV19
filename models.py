"""
Modelo Django para armazenar registros de casos de COVID-19.

Representa os dados diários de casos confirmados e óbitos.
"""

from django.db import models


class CovidRecord(models.Model):
    """Modelo que representa um registro diário de COVID-19."""

    # Data da observação
    date = models.DateField()

    # Número acumulado de casos confirmados até a data
    confirmed = models.IntegerField()

    # Número acumulado de óbitos até a data
    deaths = models.IntegerField()

    # Número de novos casos registrados no dia
    new_cases = models.IntegerField()

    # Número de novos óbitos registrados no dia
    new_deaths = models.IntegerField()

    class Meta:
        """Configurações adicionais do modelo."""
        ordering = ['-date']  # Ordena do mais recente para o mais antigo
        verbose_name = "Registro de COVID-19"
        verbose_name_plural = "Registros de COVID-19"

    def __str__(self):
        """Representação textual do registro."""
        return f"{self.date} - {self.confirmed} casos"
