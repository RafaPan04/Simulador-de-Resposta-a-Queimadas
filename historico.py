"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Gerenciamento de Histórico

Este módulo implementa uma classe genérica para gerenciar histórico de eventos,
utilizando uma estrutura de pilha para manter o registro cronológico.
"""

from typing import TypeVar, Generic, List

T = TypeVar('T')

class Historico(Generic[T]):
    """
    Classe genérica para gerenciar histórico de eventos.
    
    Esta classe implementa uma estrutura de pilha para armazenar eventos
    em ordem cronológica, permitindo acesso ao histórico mais recente primeiro.
    
    Type Parameters:
        T: Tipo genérico dos itens a serem armazenados no histórico
    
    Atributos:
        _registros (List[T]): Lista que implementa a pilha de registros
    """
    
    def __init__(self):
        """Inicializa um histórico vazio."""
        self._registros: List[T] = []  # Pilha para histórico
        
    def registrar(self, item: T):
        """
        Adiciona um item ao histórico (push na pilha).
        
        Args:
            item (T): Item a ser registrado no histórico
        """
        self._registros.append(item)
        
    def listar(self):
        """
        Lista o histórico (do mais recente para o mais antigo) e retorna a lista.
        
        Returns:
            List[T]: Lista dos registros em ordem cronológica reversa
        """
        if not self._registros:
            print("❌ Histórico vazio ❌")
            return []
                
        return list(reversed(self._registros))
                
    def esta_vazio(self) -> bool:
        """
        Verifica se o histórico está vazio.
        
        Returns:
            bool: True se o histórico estiver vazio, False caso contrário
        """
        return len(self._registros) == 0
        
   
        