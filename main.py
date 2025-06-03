"""
Sistema de Gerenciamento de Ocorrências de Queimadas - Interface Principal

Este módulo implementa a interface de usuário do sistema, fornecendo um menu interativo
para gerenciar ocorrências de queimadas, equipes e atendimentos.
"""

from central_atendimento import CentralAtendimento
from ocorrencia import Ocorrencia
from equipe import Equipe


def exibir_menu():
    """
    Exibe o menu principal do sistema com todas as opções disponíveis.
    Retorna a opção escolhida pelo usuário.
    """
    print("\n" + "="*50)
    print("🔥 SISTEMA DE GERENCIAMENTO DE QUEIMADAS 🔥")
    print("="*50)
    print("\n📋 MENU DE AÇÕES:")
    print("1. ➕ Adicionar uma nova ocorrência")
    print("2. 🚒 Atender ocorrência (atenderá a ocorrência com maior prioridade na fila)")
    print("3. 🔄 Atualizar status de ocorrência")
    print("4. 🔍 Buscar detalhes de ocorrência")
    print("5. 📊 Buscar lista de ocorrências por grau de severidade")
    print("6. 📝 Listar todas as ocorrências registradas")
    print("7. 📈 Listar histórico de atendimentos de todas as equipes")
    print("0. ❌ Sair")
    print("\n" + "-"*50)
    return input("👉 Escolha uma opção: ")

def gerenciar_equipes(central):
    """
    Gerencia o cadastro inicial de equipes no sistema.
    
    Args:
        central (CentralAtendimento): Instância da central de atendimento
    """
    print("\n" + "="*50)
    print("👥 GERENCIAMENTO DE EQUIPES")
    print("="*50)
    print("Bem-vindo ao sistema de gerenciamento de equipes ao combate de queimadas!")
    print("-"*50)
    
    while True:
        print("\n📋 OPÇÕES:")
        print("1. ➕ Adicionar nova equipe")
        print("2. ✅ Finalizar cadastro de equipes")
        opcao = input("\n👉 Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("\n📝 Nome da equipe: ")
            equipe = Equipe(nome)
            central.adicionar_equipe(equipe)
            print(f"\n✅ Equipe '{nome}' adicionada com sucesso!")
        elif opcao == "2":
            if not central.equipes:
                print("\n⚠️ É necessário adicionar pelo menos uma equipe!")
                continue
            print("\n✅ Cadastro de equipes finalizado!")
            break
        else:
            print("\n❌ Opção inválida!")

def selecionar_equipe(central):
    """
    Permite ao usuário selecionar uma equipe da lista de equipes disponíveis.
    
    Args:
        central (CentralAtendimento): Instância da central de atendimento
    
    Returns:
        Equipe: A equipe selecionada pelo usuário
    """
    print("\n👥 EQUIPES DISPONÍVEIS:")
    print("-"*50)
    for i, equipe in enumerate(central.equipes, 0):
        print(f"{i}. 👤 {equipe.nome}")
    
    while True:
        try:
            escolha = int(input("\n👉 Escolha o número da equipe: "))
            if escolha <= (len(central.equipes) - 1):
                return central.equipes[escolha]
            print("\n❌ Número de equipe inválido!")
        except ValueError:
            print("\n❌ Por favor, digite um número válido!")

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
                print("\n" + "="*50)
                print("📝 NOVA OCORRÊNCIA")
                print("="*50)
                regiao = input("📍 Região (Norte, Sul, Leste, Oeste, Centro): ")
                severidade = int(input("🔥 Nível de severidade (1-5), sendo 5 a maior grau de severiedade: "))
                descricao = input("📋 Descrição: ")
                
                ocorrencia = Ocorrencia(regiao, severidade, descricao)
                central.registrar_ocorrencia(ocorrencia)
                
                print("\n✅ Ocorrência registrada com sucesso!")
            except ValueError:
                print("\n❌ Erro: Severidade deve ser um número entre 1 e 5")
                
        # Atender ocorrência
        elif opcao == "2":
            ocorrencia = central.atender_proxima_ocorrencia()
            if ocorrencia:
                equipe = selecionar_equipe(central)
                ocorrencia.atribuir_equipe(equipe)
                equipe.adicionar_ocorrencia_registrada(ocorrencia)
                print(f"\n✅ Atendendo ocorrência #{ocorrencia.id} em {ocorrencia.regiao} com a equipe {ocorrencia.equipe_atendimento.nome}")
            else:
                print("\nℹ️ Não há ocorrências pendentes!")
                
        # Atualizar status de ocorrência 
        elif opcao == "3":
            print("\n" + "="*50)
            print("🔄 ATUALIZAR STATUS")
            print("="*50)
            id_ocorrencia = int(input("🔢 ID da ocorrência: "))
            novo_status = input("📊 Novo status (pendente/em_atendimento/resolvida): ")
            central.atualizar_status_ocorrencia(id_ocorrencia, novo_status)
            
        # Buscar detalhes de ocorrência
        elif opcao == "4":
            print("\n" + "="*50)
            print("🔍 BUSCAR OCORRÊNCIA")
            print("="*50)
            id_ocorrencia = int(input("🔢 ID da ocorrência: "))
            ocorrencia = central.buscar_ocorrencia(id_ocorrencia)
            if ocorrencia:
                print("\n" + "-"*50)
                print(ocorrencia.__str__())
                print("-"*50)
            else:
                print("\n❌ Ocorrência não encontrada!")
                
        # Buscar lista de ocorrências por grau de severidade
        elif opcao == "5":
            try:
                print("\n" + "="*50)
                print("📊 OCORRÊNCIAS POR SEVERIDADE")
                print("="*50)
                severidade = int(input("🔥 Nível de severidade (1-5): "))
                central.listar_ocorrencias_por_severidade(severidade)
            except ValueError:
                print("\n❌ Erro: Severidade deve ser um número entre 1 e 5")
                
        # Listar todas as ocorrências registradas
        elif opcao == "6":
            print("\n" + "="*50)
            print("📝 TODAS AS OCORRÊNCIAS")
            print("="*50)
            central.listar_completamente_ocorrencias_registradas()
                    
        # Listar histórico de atendimentos de uma equipe
        elif opcao == "7":
            print("\n" + "="*50)
            print("📈 HISTÓRICO DE ATENDIMENTOS")
            print("="*50)
            for equipe in central.equipes:
                equipe.listar_historico()

        # Sair do sistema
        elif opcao == "0":
            print("\n" + "="*50)
            print("👋 Encerrando o sistema...")
            print("="*50)
            break
            
        else:
            print("\n❌ Opção inválida!")

if __name__ == "__main__":
    main() 