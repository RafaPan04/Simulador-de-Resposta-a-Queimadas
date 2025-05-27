from datetime import datetime
from historico import Historico

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
        self.historico_acoes_registradas = Historico[tuple[datetime, str]]()  # Histórico de ações
        self.tempo_espera = 0  # em minutos
        
    def registrar_acao(self, acao):
        """Registra uma ação no histórico da ocorrência"""
        timestamp = datetime.now()
        self.historico_acoes_registradas.registrar((timestamp, acao))
        
    def listar_historico_acoes(self):
        """Lista o histórico de ações"""
        print(f"\nHistórico de ações da Ocorrência #{self.id}:")
        self.historico_acoes_registradas.listar(
            formatter=lambda item: f"[{item[0].strftime('%d/%m/%Y %H:%M:%S')}] {item[1]}"
        )
        
    def atualizar_status(self, novo_status):
        """Atualiza o status da ocorrência e registra timestamps relevantes"""
        self.status = novo_status
        if novo_status == "em_atendimento" and not self.data_atendimento:
            self.data_atendimento = datetime.now()
        elif novo_status == "resolvida" and not self.data_resolucao:
            self.data_resolucao = datetime.now()
            
    def calcular_tempo_espera(self):
        """Calcula o tempo de espera em minutos"""
        if self.data_atendimento:
            return (self.data_atendimento - self.data_registro).total_seconds() / 60
        return (datetime.now() - self.data_registro).total_seconds() / 60
    
    def __str__(self):
        """Retorna uma representação em string da ocorrência"""
        return f"""
Ocorrência #{self.id}
Região: {self.regiao}
Severidade: {self.severidade}
Status: {self.status}
Descrição: {self.descricao}
Data de Registro: {self.data_registro.strftime('%d/%m/%Y %H:%M:%S')}
Tempo de Espera: {self.calcular_tempo_espera():.2f} minutos
""" 