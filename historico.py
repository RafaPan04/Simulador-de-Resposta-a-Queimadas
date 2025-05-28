from datetime import datetime
from typing import TypeVar, Generic, List, Tuple, Any

T = TypeVar('T')

class Historico(Generic[T]):
    def __init__(self):
        self._registros: List[T] = []  # Pilha para histórico
        
    def registrar(self, item: T):
        """Adiciona um item ao histórico (push na pilha)"""
        self._registros.append(item)
        
    def listar(self):
        """Lista o histórico (do mais recente para o mais antigo) e retorna a lista"""
        if not self._registros:
            print("Histórico vazio")
            return []
                
        return list(reversed(self._registros))
                
    def esta_vazio(self) -> bool:
        """Verifica se o histórico está vazio"""
        return len(self._registros) == 0
        
    def tamanho(self) -> int:
        """Retorna o tamanho do histórico"""
        return len(self._registros)
        
    def __str__(self):
        """Retorna uma representação em string do histórico"""
        if self.esta_vazio():
            return "Histórico vazio"
        return f"Histórico com {self.tamanho()} registros" 