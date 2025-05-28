import heapq
from datetime import datetime
from ocorrencia import Ocorrencia

class FilaPrioridade:
    def __init__(self):
        self._fila = []  # Heap para priorização de ocorrências
        
    def adicionar(self, ocorrencia: Ocorrencia):
        """Adiciona uma ocorrência à fila de prioridade"""
        # Calcula prioridade baseada na severidade e tempo de espera
        prioridade = (-ocorrencia.severidade, ocorrencia.data_registro)
        heapq.heappush(self._fila, (prioridade, ocorrencia))
        
    def remover_proxima(self) -> Ocorrencia:
        """Remove e retorna a próxima ocorrência com maior prioridade"""
        if not self._fila:
            return None
        _, ocorrencia = heapq.heappop(self._fila)
        return ocorrencia
        
    def esta_vazia(self) -> bool:
        """Verifica se a fila está vazia"""
        return len(self._fila) == 0
        
    def tamanho(self) -> int:
        """Retorna o tamanho da fila"""
        return len(self._fila)
        
    def __str__(self):
        """Retorna uma representação em string da fila"""
        if self.esta_vazia():
            return "Fila de prioridade vazia"
            
        ocorrencias = [f"Ocorrência #{o.id} - Severidade: {o.severidade}" 
                      for _, o in sorted(self._fila)]
        return "\n".join(ocorrencias) 