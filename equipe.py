from ocorrencia import Ocorrencia
from historico import Historico
class Equipe:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade  # Número máximo de ocorrências simultâneas
        self.ocorrencias_atuais: list[Ocorrencia] = []  # Lista de ocorrências em atendimento
        self.historico_ocorrencias_registradas = Historico[Ocorrencia]()  # Pilha para histórico de atendimentos
        
    def pode_atender(self):
        """Verifica se a equipe pode atender mais ocorrências"""
        return len(self.ocorrencias_atuais) < self.capacidade
    
    def adicionar_ocorrencia(self, ocorrencia):
        """Adiciona uma ocorrência para atendimento"""
        if self.pode_atender():
            self.ocorrencias_atuais.append(ocorrencia)
            self.historico_ocorrencias_registradas.registrar(ocorrencia)  # Push na pilha
            return True
        return False
    
    def remover_ocorrencia(self, ocorrencia):
        """Remove uma ocorrência da lista de atendimentos"""
        if ocorrencia in self.ocorrencias_atuais:
            self.ocorrencias_atuais.remove(ocorrencia)
            return True
        return False
    
    def listar_historico(self):
        """Lista o histórico de atendimentos da equipe (do mais recente para o mais antigo)"""
        print(f"\nHistórico da Equipe {self.nome}:")
        for ocorrencia in self.historico_ocorrencias_registradas.listar():  # Inverte a ordem para mostrar do mais recente
            print(f"Ocorrência #{ocorrencia.id} - {ocorrencia.regiao} - Severidade: {ocorrencia.severidade}")
            
    def __str__(self):
        return f"Equipe {self.nome} - Atendendo {len(self.ocorrencias_atuais)}/{self.capacidade} ocorrências" 