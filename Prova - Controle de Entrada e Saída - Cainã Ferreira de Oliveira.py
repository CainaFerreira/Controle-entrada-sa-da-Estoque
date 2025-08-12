import os

limpa_tela = lambda: os.system('cls')
limpa_tela()

from entrada_dados import pega_string_nao_vazia ,pega_inteiro_positivo ,ler_arquivo ,escrever_arquivo ,garantir_arquivo_existe

arquivoe = 'estoque.txt'
arquivosol = 'produtos_solicitados.txt'

def menu():
    print("======= Controle de Estoque =======")
    print("1. Cadastrar um produto")
    print("2. Listar Estoque")
    print("3. Listar Produtos Solicitados")
    print("4. Remover um produto do estoque")
    print("5. Entrada e Saída de Produtos")
    print("6. Sair")

def gerar_id_arquivo(arquivoe):
    linhas = ler_arquivo(arquivoe)
    if not linhas:
        return 1
    ids = [int(linha.split(":")[0]) for linha in linhas]
    return max(ids) + 1

def gerar_id_solicitados(arquivosol):
    linhas = ler_arquivo(arquivosol)
    if not linhas:
        return 1
    ids = [int(linha.split(":")[0]) for linha in linhas]
    return max(ids) + 1

def cadastrar_produto():
    id_produto = gerar_id_arquivo(arquivoe)
    nome_produto = pega_string_nao_vazia("Informe o nome do produto: ")
    qtd_produto = pega_inteiro_positivo("Informe a quantidade: ")
    novo_p = f"{id_produto}:{nome_produto}:{qtd_produto}\n"
    escrever_arquivo(arquivoe, novo_p, 'a')
    print(f"'{nome_produto}' adicionado com sucesso! ID gerado: {id_produto}")

def listar_estoque():
    estoque = ler_arquivo(arquivoe)
    print("========== Produtos em Estoque ==========")
    print(f"{'ID':<10} {'Nome':<15} {'Quantidade':<15}")
    for produtos in estoque:
        id, nome, quantidade = produtos.strip().split(':')
        print(f"{id:<10} {nome:<15} {quantidade:<15}")
    print("========================================")

def listar_solicitados():
    solicitados = ler_arquivo(arquivosol)
    print("========== Produtos Solicitados ==========")
    print(f"{'ID':<10} {'Nome':<15} {'Quantidade':<15}")
    for produtos in solicitados:
        id, nome, quantidade = produtos.strip().split(':')
        print(f"{id:<10} {nome:<15} {quantidade:<15}")
    print("========================================")

def remover_produto():
    limpa_tela()
    listar_estoque()
    id_produto = pega_inteiro_positivo("Digite o ID do Produto a ser removido: ")
    linhas = ler_arquivo(arquivoe)
    conteudo_atualizado = ""
    removido = False

    for linha in linhas:
        id_linha, nome_produto, qtd_produto = linha.strip().split(":")
        if int(id_linha) != id_produto:
            conteudo_atualizado += linha
        else:
            removido = True

    escrever_arquivo(arquivoe, conteudo_atualizado)

    if removido:
        print(f"Produto com ID {id_produto} removido com sucesso!")
    else:
        print(f"Produto com ID {id_produto} não encontrado.")

def atualizacao_estoque():
    while True:
        limpa_tela()
        op = pega_string_nao_vazia("Informe a operação - 'E' para entrada de produtos e 'S' para saída de produtos: ").upper()        
        if op == 'E':  
            listar_estoque()
            id_produto = pega_inteiro_positivo("Digite o ID do Produto a ser atualizado: ")
            linhas = ler_arquivo(arquivoe)
            conteudo_atualizado = ""
            conteudo_solicitado = ""
            atualizado = False 
            for linha in linhas:
                id_linha, nome_produto, quantidade = linha.strip().split(":")
                quantidade = int(quantidade) 
                if int(id_linha) == id_produto:
                    nova_quantidade = pega_inteiro_positivo("Digite a quantidade: ")
                    quantidade_atualizada = quantidade + nova_quantidade
                    conteudo_atualizado += f"{id_linha}:{nome_produto}:{quantidade_atualizada}\n"
                    atualizado = True
                else:
                    conteudo_atualizado += linha         
            escrever_arquivo(arquivoe, conteudo_atualizado)           
            if atualizado:
                print(f"Produto com ID {id_produto} atualizado com sucesso!")
            else:
                print(f"Produto com ID {id_produto} não encontrado.")
            break    
        elif op == 'S': 
            listar_estoque()
            id_produto = pega_inteiro_positivo("Digite o ID do Produto a ser atualizado: ")
            linhas = ler_arquivo(arquivoe)
            conteudo_atualizado = ""
            conteudo_solicitado = ""
            atualizado = False
            for linha in linhas:
                id_linha, nome_produto, quantidade = linha.strip().split(":")
                quantidade = int(quantidade)
                if int(id_linha) == id_produto:
                    nova_quantidade = pega_inteiro_positivo("Digite a quantidade: ")
                    quantidade_atualizada = quantidade - nova_quantidade                   
                    if quantidade_atualizada < quantidade: 
                        quantidade_solicitada = quantidade_atualizada *(-1)
                        conteudo_solicitado += f"{id_linha}:{nome_produto}:{quantidade_solicitada}\n"
                        escrever_arquivo(arquivosol, conteudo_solicitado)                    
                    conteudo_atualizado += f"{id_linha}:{nome_produto}:{quantidade_atualizada}\n"
                    atualizado = True
                else:
                    conteudo_atualizado += linha   
            escrever_arquivo(arquivoe, conteudo_atualizado)        
            escrever_arquivo(arquivosol, conteudo_solicitado)
        if atualizado:
            print(f"Produto com ID {id_produto} atualizado com sucesso!")
        else:
            print(f"Produto com ID {id_produto} não encontrado.")
            break
        break

#Programa Principal

garantir_arquivo_existe(arquivoe)
garantir_arquivo_existe(arquivosol)

while True:
    limpa_tela()
    menu()
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        if os.path.getsize(arquivoe) > 0:
            listar_estoque()
        else:
            print(f"Arquivo de '{arquivoe}' vazio")
    elif opcao == '3':
        if os.path.getsize(arquivoe) > 0:
            listar_solicitados()
        else:
            print(f"Arquivo de '{arquivosol}' vazio")
    elif opcao == '4':
        if os.path.getsize(arquivoe) > 0:
            remover_produto()
        else:
            print(f"Arquivo de '{arquivoe}' vazio")
    elif opcao == '5':
        atualizacao_estoque()
    elif opcao == '6':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")
    input("\nPressione <enter> para continuar")