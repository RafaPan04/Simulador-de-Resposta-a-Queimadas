"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Central de Atendimento

Este módulo implementa a classe CentralAtendimento, que é o núcleo do sistema.
Gerencia todas as operações relacionadas a ocorrências, equipes e priorização de atendimentos.
"""

from ocorrencia import Ocorrencia
from equipe import Equipe
from fila_prioridade import FilaPrioridade

class CentralAtendimento:
    """
    Classe principal que gerencia todo o sistema de atendimento a queimadas.
    
    Atributos:
        ocorrencias (dict): Dicionário que mapeia IDs para ocorrências (busca O(1))
        fila_prioridade (FilaPrioridade): Heap para gerenciar prioridade de atendimentos
        equipes (list): Lista de equipes disponíveis
        regioes (set): Conjunto de regiões atendidas
        ocorrencias_por_severidade (list): Lista ordenada para busca binária por severidade
    """
    
    def __init__(self):
        """Inicializa a central de atendimento com estruturas de dados vazias."""
        self.ocorrencias: dict[int, Ocorrencia] = {}  # Dicionário para busca rápida por ID para opção 4: "Buscar detalhes de ocorrência"
        self.fila_prioridade = FilaPrioridade()  # Fila de prioridade para ocorrências
        self.equipes: list[Equipe] = []  # Lista de equipes disponíveis
        self.ocorrencias_por_severidade = []  # Lista ordenada para busca binária e opção 5: "Buscar lista de ocorrências por grau de severidade" 
        
    def adicionar_equipe(self, equipe):
        """
        Adiciona uma nova equipe ao sistema.
        
        Args:
            equipe (Equipe): Equipe a ser adicionada
        """
        self.equipes.append(equipe)
        
    def registrar_ocorrencia(self, ocorrencia):
        """
        Registra uma nova ocorrência no sistema.
        
        Args:
            ocorrencia (Ocorrencia): Ocorrência a ser registrada
        """
        # Adiciona ao dicionário para busca rápida por ID
        self.ocorrencias[ocorrencia.id] = ocorrencia
        
        # Adiciona à fila de prioridade para atendimento
        self.fila_prioridade.adicionar(ocorrencia)
        
        # Adiciona à lista ordenada para busca binária por severidade
        self.ocorrencias_por_severidade.append(ocorrencia)
        self.ocorrencias_por_severidade.sort(key=lambda x: x.severidade)
        
    def buscar_por_severidade(self, severidade) -> list[Ocorrencia] | list:
        """
        Busca ocorrências por severidade usando busca binária.
        
        Args:
            severidade (int): Nível de severidade a ser buscado
            
        Returns:
            list[Ocorrencia]: Lista de ocorrências com a severidade especificada

        Raises:
            ValueError: Se a severidade não estiver entre 1 e 5
        """
        if not isinstance(severidade, int) or not 1 <= severidade <= 5:
            raise ValueError("Severidade deve ser um número inteiro entre 1 e 5")
            
        if not self.ocorrencias_por_severidade:
            return []
            
        # Implementação da busca binária
        inicio = 0
        fim = len(self.ocorrencias_por_severidade) - 1
        primeiro_indice = -1
        
        # Encontra o primeiro índice com a severidade desejada
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
        """
        Lista todas as ocorrências de uma determinada severidade.
        
        Args:
            severidade (int): Nível de severidade a ser listado
        """
        ocorrencias = self.buscar_por_severidade(severidade)
        if not ocorrencias:
            print("\n" + "="*50)
            print(f"ℹ️  Nenhuma ocorrência com severidade {severidade} encontrada")
            print("="*50)
            return
        print("\n" + "="*50)
        print(f"📊 OCORRÊNCIAS COM SEVERIDADE {severidade}")
        print("="*50)
        for ocorrencia in ocorrencias:
            ocorrencia.exibir_resumo()

    def atender_proxima_ocorrencia(self) -> Ocorrencia | None:
        """
        Atende a próxima ocorrência com maior prioridade.
        
        Returns:
            Ocorrencia | None: A próxima ocorrência a ser atendida ou None se não houver ocorrências
        """
        if self.fila_prioridade.esta_vazia():
            return None

        ocorrencia = self.fila_prioridade.remover_proxima()
        return ocorrencia
    
    def listar_completamente_ocorrencias_registradas(self):
        """Lista o histórico de todas as ocorrências registradas no sistema."""
        if not self.ocorrencias:
            print("\n" + "="*50)
            print("ℹ️  Não há ocorrências registradas no sistema")
            print("="*50)
            return
            
        print("\n" + "="*50)
        print("📋 TODAS AS OCORRÊNCIAS REGISTRADAS")
        print("="*50)
        for ocorrencia in self.ocorrencias.values():
            print(ocorrencia.__str__())
            
    def concluir_ocorrencia(self, id_ocorrencia):
        """
        Atualiza o status de uma ocorrência específica.
        
        Args:
            id_ocorrencia (int): ID da ocorrência
        """
        if id_ocorrencia in self.ocorrencias:
            ocorrencia = self.ocorrencias[id_ocorrencia]
            ocorrencia.atualizar_status("resolvida")
            print("\n" + "="*50)
            print(f"✅ Ocorrência #{id_ocorrencia} concluída")
            print("="*50)
        else:
            print("\n" + "="*50)
            print(f"❌ Ocorrência #{id_ocorrencia} não encontrada")
            print("="*50)

    def buscar_ocorrencia(self, id_ocorrencia):
        """
        Busca uma ocorrência pelo ID usando busca em dicionário O(1).
        
        Args:
            id_ocorrencia (int): ID da ocorrência a ser buscada
            
        Returns:
            Ocorrencia | None: A ocorrência encontrada ou None se não existir
        """
        return self.ocorrencias.get(id_ocorrencia)


