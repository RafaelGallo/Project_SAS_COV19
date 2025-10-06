"""
Serializer para o modelo CovidRecord.

Responsável por converter objetos do modelo CovidRecord
em representações JSON e vice-versa.
"""

from rest_framework import serializers
from .models import CovidRecord


class CovidRecordSerializer(serializers.ModelSerializer):
    """
    Serializer baseado em ModelSerializer para o modelo CovidRecord.

    Este serializer expõe todos os campos do modelo, permitindo
    leitura e escrita completas (CRUD) via API REST.
    """

    class Meta:
        """Configuração do serializer."""
        model = CovidRecord        # Modelo associado
        fields = '__all__'         # Inclui todos os campos do modelo
