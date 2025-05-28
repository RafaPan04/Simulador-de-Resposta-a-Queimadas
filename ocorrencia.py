from datetime import datetime
from historico import Historico
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from equipe import Equipe

class Ocorrencia:
    _id_counter = 1
    
    def __init__(self, regiao, severidade, descricao):
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
        """Atribui uma equipe para atender a ocorrência"""
        if self.equipe_atendimento is not None:
            return False
            
        self.equipe_atendimento = equipe
        self.atualizar_status("em_atendimento")
        return True
        
    def atualizar_status(self, novo_status):
        """Atualiza o status da ocorrência e registra timestamps relevantes"""
        self.status = novo_status
        if novo_status == "em_atendimento" and not self.data_atendimento:
            self.data_atendimento = datetime.now()
        elif novo_status == "resolvida" and not self.data_resolucao:
            self.data_resolucao = datetime.now()
            
    def exibir_resumo(self):
        """Exibe um resumo da ocorrência"""
        equipe_info = f" - Equipe: {self.equipe_atendimento.nome}" if self.equipe_atendimento else ""
        print(f"Ocorrência #{self.id} - Região: {self.regiao} - Severidade: {self.severidade} - Status: {self.status}{equipe_info}")

    def __str__(self):
        """Retorna uma representação em string da ocorrência"""
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