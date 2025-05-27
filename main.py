from central_atendimento import CentralAtendimento
from ocorrencia import Ocorrencia
from equipe import Equipe
import random
import time
from datetime import datetime

def exibir_menu():
    print("\n=== SIMULADOR DE RESPOSTA A QUEIMADAS ===")
    print("1. Gerenciar Equipes")
    print("2. Adicionar uma nova ocorrência")
    print("3. Atender ocorrência (atenderá a ocorrência com maior prioridade)")
    print("4. Atualizar status de ocorrência")
    print("5. Gerar relatório por região")
    # print("6. Simular chamadas aleatórias")
    print("7. Buscar detalhes de ocorrência")
    print("8. Buscar ocorrências por grau de severidade")
    print("0. Sair")
    return input("Escolha uma opção: ")

def exibir_menu_equipes():
    print("\n=== GERENCIAMENTO DE EQUIPES ===")
    print("1. Adicionar nova equipe")
    print("2. Listar equipes")
    print("3. Listar histórico de atendimentos")
    print("0. Voltar ao menu principal")
    return input("Escolha uma opção: ")

def gerenciar_equipes(central):
    while True:
        opcao = exibir_menu_equipes()
        
        if opcao == "1":
            nome = input("Nome da equipe: ")
            try:
                capacidade = int(input("Capacidade da equipe (número de ocorrências simultâneas): "))
                if capacidade <= 0:
                    print("Erro: A capacidade deve ser maior que zero!")
                    continue
                    
                equipe = Equipe(nome, capacidade)
                central.adicionar_equipe(equipe)
                print(f"Equipe {nome} adicionada com sucesso!")
            except ValueError:
                print("Erro: A capacidade deve ser um número inteiro!")
                
        elif opcao == "2":
            if not central.equipes:
                print("Não há equipes cadastradas!")
            else:
                print("\nEquipes cadastradas:")
                for i, equipe in enumerate(central.equipes, 1):
                    print(f"{i}. {equipe}")
        
        elif opcao == "3":
            central.listar_historico_equipe()     

        elif opcao == "0":
            break
            
        else:
            print("Opção inválida!")

def verificar_equipes(central):
    """Verifica se existem equipes cadastradas"""
    if not central.equipes:
        print("\nATENÇÃO: Não há equipes cadastradas!")
        print("Por favor, cadastre pelo menos uma equipe antes de continuar.")
        gerenciar_equipes(central)
        return False
    return True

def main():
    central = CentralAtendimento()
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            gerenciar_equipes(central)
            
        elif opcao == "2":
           
                try:
                    regiao = input("Região: ")
                    severidade = int(input("Nível de severidade (1-5): "))
                    descricao = input("Descrição: ")
                    
                    ocorrencia = Ocorrencia(regiao, severidade, descricao)
                    central.registrar_ocorrencia(ocorrencia)
                    print("Ocorrência registrada com sucesso!")
                except ValueError:
                    print("Erro: Severidade deve ser um número entre 1 e 5")
                    
        elif opcao == "3":
            if verificar_equipes(central):
                ocorrencia = central.atender_proxima_ocorrencia()
                if ocorrencia:
                    print(f"Atendendo ocorrência #{ocorrencia.id} em {ocorrencia.regiao}")
                else:
                    print("Não há ocorrências pendentes!")
                    
        
                
        elif opcao == "4":
            if verificar_equipes(central):
                id_ocorrencia = int(input("ID da ocorrência: "))
                novo_status = input("Novo status (pendente/em_atendimento/resolvida): ")
                central.atualizar_status(id_ocorrencia, novo_status)
                
        elif opcao == "5":
            if verificar_equipes(central):
                regiao = input("Região para relatório: ")
                central.gerar_relatorio_regiao(regiao)
                
        # elif opcao == "6":
        #     if verificar_equipes(central):
        #         num_simulacoes = int(input("Número de simulações: "))
        #         central.simular_chamadas(num_simulacoes)
                
        elif opcao == "7":
            if verificar_equipes(central):
                id_ocorrencia = int(input("ID da ocorrência: "))
                ocorrencia = central.buscar_ocorrencia(id_ocorrencia)
                if ocorrencia:
                    print(ocorrencia)
                else:
                    print("Ocorrência não encontrada!")
                    
        elif opcao == "8":
            if verificar_equipes(central):
                try:
                    severidade = int(input("Nível de severidade (1-5): "))
                    central.listar_ocorrencias_por_severidade(severidade)
                except ValueError:
                    print("Erro: Severidade deve ser um número entre 1 e 5")
                    
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
            
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 