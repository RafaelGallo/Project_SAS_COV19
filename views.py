"""
ViewSet para o modelo CovidRecord.

Fornece endpoints somente leitura (GET) para listar e detalhar
registros de COVID-19 armazenados no banco de dados.
"""

from rest_framework import viewsets
from .models import CovidRecord
from .serializers import CovidRecordSerializer


class CovidRecordViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet somente leitura para o modelo CovidRecord.

    Permite as operações:
    - GET /covidrecords/  → lista todos os registros
    - GET /covidrecords/<id>/  → detalha um registro específico
    """

    # Consulta base utilizada pelo ViewSet
    queryset = CovidRecord.objects.all().order_by('-date')

    # Serializer responsável pela conversão dos dados
    serializer_class = CovidRecordSerializer
