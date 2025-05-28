"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Classe Equipe

Este módulo implementa a classe Equipe, que representa uma equipe de atendimento
responsável por responder às ocorrências de queimadas.
"""

from typing import TYPE_CHECKING
from historico import Historico

if TYPE_CHECKING:
    from ocorrencia import Ocorrencia

class Equipe:
    """
    Classe que representa uma equipe de atendimento a queimadas.
    
    Atributos:
        nome (str): Nome da equipe
        historico_ocorrencias_registradas (Historico): Histórico de ocorrências atendidas
    """
    
    def __init__(self, nome):
        """
        Inicializa uma nova equipe.
        
        Args:
            nome (str): Nome da equipe
        """
        self.nome = nome
        self.historico_ocorrencias_registradas = Historico["Ocorrencia"]() 

    def adicionar_ocorrencia_registrada(self, ocorrencia: "Ocorrencia"):
        """
        Adiciona uma ocorrência ao histórico de atendimentos da equipe.
        
        Args:
            ocorrencia (Ocorrencia): Ocorrência a ser registrada no histórico
        """
        self.historico_ocorrencias_registradas.registrar(ocorrencia)

    def listar_historico(self):
        """
        Lista o histórico de atendimentos da equipe, do mais recente para o mais antigo.
        Exibe uma mensagem se a equipe ainda não atendeu nenhuma ocorrência.
        """
        if(self.historico_ocorrencias_registradas.esta_vazio() == False):
            print(f"\nHistórico da Equipe {self.nome}:")
            for ocorrencia in self.historico_ocorrencias_registradas.listar():  
                print(f"Ocorrência #{ocorrencia.id} - {ocorrencia.regiao} - Severidade: {ocorrencia.severidade}")
        else:
            print(f"\n\nA Equipe '{self.nome}' ainda não possui nenhuma ocorrência registrada")