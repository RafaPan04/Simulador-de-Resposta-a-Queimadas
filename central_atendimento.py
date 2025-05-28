import heapq
from datetime import datetime
import random
import time
from ocorrencia import Ocorrencia
from equipe import Equipe
from fila_prioridade import FilaPrioridade

class CentralAtendimento:
    def __init__(self):
        self.ocorrencias: dict[int, Ocorrencia] = {}  # Dicionário para busca rápida por ID
        self.fila_prioridade = FilaPrioridade()  # Fila de prioridade para ocorrências
        self.equipes: list[Equipe] = []  # Lista de equipes disponíveis
        self.regioes = set()  # Conjunto de regiões atendidas
        self.ocorrencias_por_severidade = []  # Lista ordenada para busca binária
        
    def adicionar_equipe(self, equipe):
        """Adiciona uma equipe ao sistema"""
        self.equipes.append(equipe)
        
    def registrar_ocorrencia(self, ocorrencia):
        """Registra uma nova ocorrência no sistema"""
        self.ocorrencias[ocorrencia.id] = ocorrencia
        self.regioes.add(ocorrencia.regiao)
        
        # Adiciona à fila de prioridade
        self.fila_prioridade.adicionar(ocorrencia)
        
        # Adiciona à lista ordenada por severidade
        self.ocorrencias_por_severidade.append(ocorrencia)
        self.ocorrencias_por_severidade.sort(key=lambda x: x.severidade)
        
    def buscar_por_severidade(self, severidade):
        """Busca ocorrências por severidade usando busca binária"""
        if not self.ocorrencias_por_severidade:
            return []
            
        # Encontra o primeiro índice com a severidade desejada
        inicio = 0
        fim = len(self.ocorrencias_por_severidade) - 1
        primeiro_indice = -1
        
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if self.ocorrencias_por_severidade[meio].severidade == severidade:
                primeiro_indice = meio
                fim = meio - 1
            elif self.ocorrencias_por_severidade[meio].severidade < severidade:
                inicio = meio + 1
            else:
                fim = meio - 1
                
        if primeiro_indice == -1:
            return []
            
        # Coleta todas as ocorrências com a mesma severidade
        resultado = []
        i = primeiro_indice
        while i < len(self.ocorrencias_por_severidade) and self.ocorrencias_por_severidade[i].severidade == severidade:
            resultado.append(self.ocorrencias_por_severidade[i])
            i += 1
            
        return resultado
        
    def listar_ocorrencias_por_severidade(self, severidade):
        """Lista todas as ocorrências de uma determinada severidade"""
        ocorrencias = self.buscar_por_severidade(severidade)
        if not ocorrencias:
            print(f"Nenhuma ocorrência com severidade {severidade} encontrada")
            return
        print(f"\nOcorrências com severidade {severidade}:")
        for ocorrencia in ocorrencias:
            ocorrencia.exibir_resumo()

    def atender_proxima_ocorrencia(self) -> Ocorrencia | None:
        """Atende a próxima ocorrência com maior prioridade"""
        if self.fila_prioridade.esta_vazia():
            return None

        ocorrencia = self.fila_prioridade.remover_proxima()
        return ocorrencia   
    
            
    # def registrar_acao(self, id_ocorrencia, acao):
    #     """Registra uma ação em uma ocorrência específica"""
    #     if id_ocorrencia in self.ocorrencias:
    #         self.ocorrencias[id_ocorrencia].registrar_acao(acao)
    #         return True
    #     return False
        
    def listar_completamente_ocorrencias_registradas(self):
        """Lista o histórico de todas as ocorrências registradas"""
        for ocorrencia in self.ocorrencias.values():
            print(ocorrencia.__str__())
            
    def atualizar_status_ocorrencia(self, id_ocorrencia, novo_status):
        """Atualiza o status de uma ocorrência"""
        if id_ocorrencia in self.ocorrencias:
            ocorrencia = self.ocorrencias[id_ocorrencia]
            ocorrencia.atualizar_status(novo_status)

            # Se resolvida, remove a equipe
           

    # def gerar_relatorio_regiao(self, regiao):
        """Gera relatório de atendimentos por região"""
        ocorrencias_regiao = [o for o in self.ocorrencias.values() if o.regiao == regiao]
        
        print(f"\nRelatório da Região: {regiao}")
        print(f"Total de ocorrências: {len(ocorrencias_regiao)}")
        
        if ocorrencias_regiao:
            tempo_medio = sum(o.calcular_tempo_espera() for o in ocorrencias_regiao) / len(ocorrencias_regiao)
            print(f"Tempo médio de atendimento: {tempo_medio:.2f} minutos")
            
            severidades = [o.severidade for o in ocorrencias_regiao]
            print(f"Severidade média: {sum(severidades)/len(severidades):.1f}")
            
    def buscar_ocorrencia(self, id_ocorrencia):
        """Busca uma ocorrência pelo ID usando busca em dicionário O(1)"""
        return self.ocorrencias.get(id_ocorrencia) 