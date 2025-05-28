from central_atendimento import CentralAtendimento
from ocorrencia import Ocorrencia
from equipe import Equipe
import random
import time
from datetime import datetime

def exibir_menu():
    print("\n=== SIMULADOR DE RESPOSTA A QUEIMADAS ===")
    print("2. Adicionar uma nova ocorrência")
    print("3. Atender ocorrência (atenderá a ocorrência com maior prioridade na fila)")
    print("4. Atualizar status de ocorrência")
    # print("6. Simular chamadas aleatórias")
    print("7. Buscar detalhes de ocorrência")
    print("8. Buscar lista de ocorrências por grau de severidade")
    print("9. Listar todas as ocorrências registradas")
    print("10. Listar histórico de atendimentos de todas as equipes")
    print("0. Sair")
    return input("Escolha uma opção: ")



def gerenciar_equipes(central):
    print("--------------------------------")
    print("Bem vindo ao gerenciamento de equipes")
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
    central = CentralAtendimento()

 
    gerenciar_equipes(central)
    while True:
        opcao = exibir_menu()
        

         ## adicionar nova ocorrencia
        if opcao == "2":
           
                try:
                    regiao = input("Região (Norte, Sul, Leste, Oeste, Centro): ")
                    severidade = int(input("Nível de severidade de 1 a 5, sendo 5 a maior grau de severiedade : "))
                    descricao = input("Descrição: ")
                    
                    ocorrencia = Ocorrencia(regiao, severidade, descricao)
                    central.registrar_ocorrencia(ocorrencia)
                    print("Ocorrência registrada com sucesso!")
                except ValueError:
                    print("Erro: Severidade deve ser um número entre 1 e 5")
                    
        ## atender ocorrência
        elif opcao == "3":
            
                ocorrencia = central.atender_proxima_ocorrencia()
                if ocorrencia:
                    equipe = selecionar_equipe(central)
                    ocorrencia.atribuir_equipe(equipe)
                    equipe.adicionar_ocorrencia_registrada(ocorrencia)
                    print(f"Atendendo ocorrência #{ocorrencia.id} em {ocorrencia.regiao} com a equipe {ocorrencia.equipe_atendimento.nome}")
                else:
                    print("Não há ocorrências pendentes!")
                    
        
                
        ## atualizar status de ocorrência 
        elif opcao == "4":
            
                id_ocorrencia = int(input("ID da ocorrência: "))
                novo_status = input("Novo status (pendente/em_atendimento/resolvida): ")
                central.atualizar_status_ocorrencia(id_ocorrencia, novo_status)
                
        ## gerar relatório por região
        # elif opcao == "5":
        #     if verificar_equipes(central):
        #         regiao = input("Região para relatório: ")
        #         central.gerar_relatorio_regiao(regiao)
                
        # elif opcao == "6":
        #     if verificar_equipes(central):
        #         num_simulacoes = int(input("Número de simulações: "))
        #         central.simular_chamadas(num_simulacoes)
                
        ## buscar detalhes de ocorrência
        elif opcao == "7":
            
                id_ocorrencia = int(input("ID da ocorrência: "))
                ocorrencia = central.buscar_ocorrencia(id_ocorrencia)
                if ocorrencia:
                    print(ocorrencia.__str__())
                else:
                    print("Ocorrência não encontrada!")
                    
        ## buscar lista de ocorrências por grau de severidade
        elif opcao == "8":
           
                try:
                    severidade = int(input("Nível de severidade (1-5): "))
                    central.listar_ocorrencias_por_severidade(severidade)
                except ValueError:
                    print("Erro: Severidade deve ser um número entre 1 e 5")
                    
        ## listar todas as ocorrências registradas
        elif opcao == "9":
            central.listar_completamente_ocorrencias_registradas()
                    
        ## listar histórico de atendimentos de uma equipe
        elif opcao == "10":
            for equipe in central.equipes:
                equipe.listar_historico()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break
            
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 