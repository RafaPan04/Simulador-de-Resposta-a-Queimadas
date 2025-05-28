# Sistema de Gerenciamento de Ocorrências de Queimadas

Este é um sistema de gerenciamento de ocorrências de queimadas que permite o registro, priorização e atendimento de incidentes por equipes de resposta. O sistema utiliza estruturas de dados eficientes para garantir um atendimento rápido e organizado das ocorrências.

## Estrutura do Projeto

O projeto é composto por vários módulos, cada um com uma responsabilidade específica:

### 1. `main.py`
Arquivo principal que contém a interface do usuário e a lógica de controle do sistema. Oferece um menu interativo com as seguintes opções:
- Adicionar nova ocorrência
- Atender ocorrência
- Atualizar status de ocorrência
- Buscar detalhes de ocorrência
- Buscar lista de ocorrências por grau de severidade
- Listar todas as ocorrências registradas
- Listar histórico de atendimentos das equipes

### 2. `central_atendimento.py`
Classe principal que gerencia todo o sistema. Responsabilidades:
- Gerenciamento de equipes
- Registro de ocorrências
- Priorização de atendimentos
- Busca e listagem de ocorrências
- Atualização de status

### 3. `ocorrencia.py`
Classe que representa uma ocorrência de queimada. Atributos:
- ID único
- Região
- Severidade (1-5)
- Descrição
- Status (pendente/em_atendimento/resolvida)
- Datas de registro, atendimento e resolução
- Equipe responsável

### 4. `equipe.py`
Classe que representa uma equipe de atendimento. Funcionalidades:
- Gerenciamento de nome da equipe
- Histórico de atendimentos
- Listagem de ocorrências atendidas

### 5. `fila_prioridade.py`
Implementação de uma fila de prioridade para gerenciar as ocorrências. Características:
- Priorização baseada na severidade e tempo de espera
- Uso de heap para eficiência
- Operações de adicionar e remover ocorrências

### 6. `historico.py`
Classe genérica para gerenciar histórico de eventos. Funcionalidades:
- Registro de eventos
- Listagem ordenada (mais recente primeiro)
- Verificação de estado vazio
- Contagem de registros

## Como Usar

1. Execute o arquivo `main.py`
2. Primeiro, cadastre pelo menos uma equipe de atendimento
3. Use o menu interativo para:
   - Registrar novas ocorrências
   - Atender ocorrências pendentes
   - Atualizar status de ocorrências
   - Consultar informações do sistema

## Características Técnicas

- Uso de estruturas de dados eficientes (heap, dicionários)
- Sistema de priorização inteligente
- Rastreamento completo de ocorrências
- Histórico detalhado de atendimentos
- Interface de usuário intuitiva

## Estruturas de Dados Utilizadas

O sistema utiliza várias estruturas de dados otimizadas para diferentes propósitos:

### 1. Heap (Fila de Prioridade)
- **Localização**: `fila_prioridade.py`
- **Uso**: Gerenciamento de ocorrências por prioridade
- **Implementação**: Utiliza o módulo `heapq` do Python
- **Complexidade**: O(log n) para inserção e remoção
- **Exemplo de uso**:
```python
def adicionar(self, ocorrencia: Ocorrencia):
    prioridade = (-ocorrencia.severidade, ocorrencia.data_registro)
    heapq.heappush(self._fila, (prioridade, ocorrencia))
```

### 2. Dicionário
- **Localização**: `central_atendimento.py`
- **Uso**: Armazenamento e busca rápida de ocorrências por ID
- **Implementação**: `self.ocorrencias: dict[int, Ocorrencia] = {}`
- **Complexidade**: O(1) para busca, inserção e remoção
- **Exemplo de uso**:
```python
def buscar_ocorrencia(self, id_ocorrencia):
    return self.ocorrencias.get(id_ocorrencia)
```

### 3. Busca Binária
- **Localização**: `central_atendimento.py`
- **Uso**: Busca eficiente de ocorrências por severidade
- **Implementação**: Lista ordenada com busca binária
- **Complexidade**: O(log n) para busca
- **Exemplo de uso**:
```python
def buscar_por_severidade(self, severidade):
    inicio = 0
    fim = len(self.ocorrencias_por_severidade) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if self.ocorrencias_por_severidade[meio].severidade == severidade:
            # Encontrou a ocorrência
            return self.ocorrencias_por_severidade[meio]
```

### 4. Lista (Pilha)
- **Localização**: `historico.py`
- **Uso**: Gerenciamento de histórico de eventos
- **Implementação**: Lista Python com operações de pilha
- **Complexidade**: O(1) para inserção e remoção do topo
- **Exemplo de uso**:
```python
def registrar(self, item: T):
    self._registros.append(item)
```

## Requisitos

- Python 3.x
- Módulos padrão do Python (datetime, heapq)

## Exemplo de Uso

1. Inicie o sistema:
```bash
python main.py
```

2. Cadastre uma equipe:
- Escolha a opção de adicionar equipe
- Digite o nome da equipe

3. Registre uma ocorrência:
- Escolha a opção de adicionar ocorrência
- Informe a região, severidade e descrição

4. Atenda a ocorrência:
- Escolha a opção de atender ocorrência
- Selecione a equipe responsável
