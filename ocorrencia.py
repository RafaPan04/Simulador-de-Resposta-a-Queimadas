"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Classe Ocorrência

Este módulo implementa a classe Ocorrencia, que representa uma ocorrência de queimada
no sistema, contendo todas as informações relevantes sobre o incidente.
"""

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from equipe import Equipe

class Ocorrencia:
    """
    Classe que representa uma ocorrência de queimada no sistema.
    
    Atributos:
        id (int): Identificador único da ocorrência
        regiao (str): Região onde ocorreu a queimada
        severidade (int): Nível de severidade (1-5)
        descricao (str): Descrição detalhada da ocorrência
        status (str): Status atual (pendente/em_atendimento/resolvida)
        data_registro (datetime): Data e hora do registro
        data_atendimento (datetime): Data e hora do início do atendimento
        data_resolucao (datetime): Data e hora da resolução
        tempo_espera (int): Tempo de espera em minutos
        equipe_atendimento (Equipe): Equipe responsável pelo atendimento
    """
    
    _id_counter = 1  # Contador estático para gerar IDs únicos
    
    def __init__(self, regiao, severidade, descricao):
        """
        Inicializa uma nova ocorrência.
        
        Args:
            regiao (str): Região da ocorrência
            severidade (int): Nível de severidade (1-5)
            descricao (str): Descrição da ocorrência
        """
        self.id = Ocorrencia._id_counter
        Ocorrencia._id_counter += 1
        
        self.regiao = regiao
        self.severidade = min(max(severidade, 1), 5)  # Garante que severidade está entre 1 e 5
        self.descricao = descricao
        self.status = "pendente"
        self.data_registro = datetime.now()
        self.data_atendimento = None
        self.data_resolucao = None
        self.tempo_espera = 0  # em minutos
        self.equipe_atendimento: "Equipe | None" = None  # Referência à equipe que está atendendo
        
    def atribuir_equipe(self, equipe: "Equipe") -> bool:
        """
        Atribui uma equipe para atender a ocorrência.
        
        Args:
            equipe (Equipe): Equipe a ser atribuída
            
        Returns:
            bool: True se a atribuição foi bem-sucedida, False caso contrário
        """
        if self.equipe_atendimento is not None:
            return False
            
        self.equipe_atendimento = equipe
        self.atualizar_status("em_atendimento")
        return True
        
    def atualizar_status(self, novo_status):
        """
        Atualiza o status da ocorrência e registra timestamps relevantes.
        
        Args:
            novo_status (str): Novo status da ocorrência
        """
        self.status = novo_status
        if novo_status == "em_atendimento" and not self.data_atendimento:
            self.data_atendimento = datetime.now()
        elif novo_status == "resolvida" and not self.data_resolucao:
            self.data_resolucao = datetime.now()
            
    def exibir_resumo(self):
        """Exibe um resumo conciso da ocorrência."""
        equipe_info = f" - Equipe: {self.equipe_atendimento.nome}" if self.equipe_atendimento else ""
        print ("======================================")
        print(f"Ocorrência #{self.id} - Região: {self.regiao} - Severidade: {self.severidade} - Status: {self.status}{equipe_info}")

    def __str__(self):
        """
        Retorna uma representação detalhada da ocorrência em formato string.
        
        Returns:
            str: Representação detalhada da ocorrência
        """
        equipe_info = f"Equipe atendendo: {self.equipe_atendimento.nome}" if self.equipe_atendimento else "Sem equipe atribuída"
        return f"""
Ocorrência #{self.id}
Região: {self.regiao}
Severidade: {self.severidade}
Status: {self.status}
{equipe_info}
Descrição: {self.descricao}
Data de Registro: {self.data_registro.strftime('%d/%m/%Y %H:%M:%S')}
"""