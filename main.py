"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Interface Principal

Este módulo implementa a interface de usuário do sistema, fornecendo um menu interativo
para gerenciar ocorrências de queimadas, equipes e atendimentos.
"""

from central_atendimento import CentralAtendimento
from ocorrencia import Ocorrencia
from equipe import Equipe
from datetime import datetime

def exibir_menu():
    """
    Exibe o menu principal do sistema com todas as opções disponíveis.
    Retorna a opção escolhida pelo usuário.
    """
    print("\n=== OPCÇÕES DE AÇÕES ===")
    print("1. Adicionar uma nova ocorrência")
    print("2. Atender ocorrência (atenderá a ocorrência com maior prioridade na fila)")
    print("3. Atualizar status de ocorrência")
    print("4. Buscar detalhes de ocorrência")
    print("5. Buscar lista de ocorrências por grau de severidade")
    print("6. Listar todas as ocorrências registradas")
    print("7. Listar histórico de atendimentos de todas as equipes")
    print("0. Sair")
    return input("Escolha uma opção: ")

def gerenciar_equipes(central):
    """
    Gerencia o cadastro inicial de equipes no sistema.
    
    Args:
        central (CentralAtendimento): Instância da central de atendimento
    """
    print("--------------------------------")
    print("Bem vindo ao gerenciamento de equipes ao combate de queimadas")
    print("--------------------------------")
    
    while True:
        print("\n1. Adicionar nova equipe")
        print("2. Finalizar cadastro de equipes")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da equipe: ")
            equipe = Equipe(nome)
            central.adicionar_equipe(equipe)
            print(f"Equipe {nome} adicionada com sucesso!")
        elif opcao == "2":
            if not central.equipes:
                print("É necessário adicionar pelo menos uma equipe!")
                continue
            print("Cadastro de equipes finalizado!")
            break
        else:
            print("Opção inválida!")

def selecionar_equipe(central):
    """
    Permite ao usuário selecionar uma equipe da lista de equipes disponíveis.
    
    Args:
        central (CentralAtendimento): Instância da central de atendimento
    
    Returns:
        Equipe: A equipe selecionada pelo usuário
    """
    print("\nEquipes disponíveis:")
    for i, equipe in enumerate(central.equipes, 0):
        print(f"{i}. {equipe.nome}")
    
    while True:
        try:
            escolha = int(input("\nEscolha o número da equipe: "))
            if escolha <= len(central.equipes):
                return central.equipes[escolha]
            print("Número de equipe inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")

def main():
    """
    Função principal que inicializa o sistema e gerencia o fluxo de execução.
    """
    # Inicializa a central de atendimento
    central = CentralAtendimento()

    # Realiza o cadastro inicial de equipes
    gerenciar_equipes(central)
    
    # Loop principal do sistema
    while True:
        opcao = exibir_menu()
        
        # Adicionar nova ocorrência
        if opcao == "1":
            try:
                regiao = input("Região (Norte, Sul, Leste, Oeste, Centro): ")
                severidade = int(input("Nível de severidade de 1 a 5, sendo 5 a maior grau de severiedade : "))
                descricao = input("Descrição: ")
                
                ocorrencia = Ocorrencia(regiao, severidade, descricao)
                central.registrar_ocorrencia(ocorrencia)
                print("Ocorrência registrada com sucesso!")
            except ValueError:
                print("Erro: Severidade deve ser um número entre 1 e 5")
                
        # Atender ocorrência
        elif opcao == "2":
            ocorrencia = central.atender_proxima_ocorrencia()
            if ocorrencia:
                equipe = selecionar_equipe(central)
                ocorrencia.atribuir_equipe(equipe)
                equipe.adicionar_ocorrencia_registrada(ocorrencia)
                print(f"Atendendo ocorrência #{ocorrencia.id} em {ocorrencia.regiao} com a equipe {ocorrencia.equipe_atendimento.nome}")
            else:
                print("Não há ocorrências pendentes!")
                
        # Atualizar status de ocorrência 
        elif opcao == "3":
            id_ocorrencia = int(input("ID da ocorrência: "))
            novo_status = input("Novo status (pendente/em_atendimento/resolvida): ")
            central.atualizar_status_ocorrencia(id_ocorrencia, novo_status)
            
        # Buscar detalhes de ocorrência
        elif opcao == "4":
            id_ocorrencia = int(input("ID da ocorrência: "))
            ocorrencia = central.buscar_ocorrencia(id_ocorrencia)
            if ocorrencia:
                print(ocorrencia.__str__())
            else:
                print("Ocorrência não encontrada!")
                
        # Buscar lista de ocorrências por grau de severidade
        elif opcao == "5":
            try:
                severidade = int(input("Nível de severidade (1-5): "))
                central.listar_ocorrencias_por_severidade(severidade)
            except ValueError:
                print("Erro: Severidade deve ser um número entre 1 e 5")
                
        # Listar todas as ocorrências registradas
        elif opcao == "6":
            central.listar_completamente_ocorrencias_registradas()
                    
        # Listar histórico de atendimentos de uma equipe
        elif opcao == "7":
            for equipe in central.equipes:
                equipe.listar_historico()

        # Sair do sistema
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
            
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 