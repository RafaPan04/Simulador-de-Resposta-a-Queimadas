from typing import TYPE_CHECKING
from historico import Historico

if TYPE_CHECKING:
    from ocorrencia import Ocorrencia

class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.historico_ocorrencias_registradas = Historico["Ocorrencia"]() 

    def adicionar_ocorrencia_registrada(self, ocorrencia: "Ocorrencia"):
        """Adiciona uma ao histórico de atendimentos uma ocorrência"""
        self.historico_ocorrencias_registradas.registrar(ocorrencia)

    def listar_historico(self):
        """Lista o histórico de atendimentos da equipe (do mais recente para o mais antigo)"""
        if(self.historico_ocorrencias_registradas.esta_vazio() == False):
            print(f"\nHistórico da Equipe {self.nome}:")
            for ocorrencia in self.historico_ocorrencias_registradas.listar():  # Inverte a ordem para mostrar do mais recente
                print(f"Ocorrência #{ocorrencia.id} - {ocorrencia.regiao} - Severidade: {ocorrencia.severidade}")
        else:
            print(f"\n\nA Equipe '{self.nome}' ainda não possui nenhuma ocorrência registrada")