"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Fila de Prioridade

Este módulo implementa uma fila de prioridade usando heap para gerenciar
a ordem de atendimento das ocorrências baseada em severidade e tempo de espera.
"""

import heapq
from ocorrencia import Ocorrencia

class FilaPrioridade:
    """
    Implementação de uma fila de prioridade usando heap para gerenciar ocorrências.
    
    A prioridade é calculada com base em dois fatores:
    1. Severidade da ocorrência (maior severidade = maior prioridade)
    2. Tempo de espera (ocorrências mais antigas têm prioridade)
    
    Atributos:
        _fila (list): Lista que implementa o heap de prioridade
    """
    
    def __init__(self):
        """Inicializa uma fila de prioridade vazia."""
        self._fila = []  # Heap para priorização de ocorrências
        
    def adicionar(self, ocorrencia: Ocorrencia):
        """
        Adiciona uma ocorrência à fila de prioridade.
        
        A prioridade é calculada como uma tupla (-severidade, data_registro),
        onde o sinal negativo na severidade faz com que ocorrências mais severas
        tenham maior prioridade.
        
        Args:
            ocorrencia (Ocorrencia): Ocorrência a ser adicionada
        """
        # Calcula prioridade baseada na severidade e tempo de espera
        prioridade = (-ocorrencia.severidade, ocorrencia.data_registro)
        heapq.heappush(self._fila, (prioridade, ocorrencia))
        
    def remover_proxima(self) -> Ocorrencia:
        """
        Remove e retorna a próxima ocorrência com maior prioridade.
        
        Returns:
            Ocorrencia | None: A próxima ocorrência a ser atendida ou None se a fila estiver vazia
        """
        if not self._fila:
            return None
        _, ocorrencia = heapq.heappop(self._fila)
        return ocorrencia
        
    def esta_vazia(self) -> bool:
        """
        Verifica se a fila está vazia.
        
        Returns:
            bool: True se a fila estiver vazia, False caso contrário
        """
        return len(self._fila) == 0
        