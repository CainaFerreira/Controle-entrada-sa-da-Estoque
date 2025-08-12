import os, json

def pega_string_nao_vazia(texto):
    while True:
        valor = input(texto).strip()
        if valor:
            return valor
        else:
            print("Erro: campo não pode ser vazio")

def pega_inteiro_positivo(texto):
    while True:
        try:
            valor = int(input(texto))
            if valor > 0:
                return valor
            else:
                print("Erro: campo não pode ser negativo")  
        except ValueError:
            print("Erro: campo deve ser um numero inteiro")


def ler_arquivo(nome_arquivo):
    #Lê o conteúdo de um arquivo e retorna como uma lista.
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.readlines()
        
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except IOError:
        print("Erro : no acesso de abertura do arquivo")
    except PermissionError:
        print("Erro : permissão de acesso ao arquivo")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
    return []

def escrever_arquivo(nome_arquivo, conteudo, modo='w'):
    #Escreve conteúdo no arquivo especificado.
    try:
        with open(nome_arquivo, modo, encoding='utf-8') as arquivo:
            arquivo.write(conteudo)

    except IOError:
        print("Erro : no acesso de abertura do arquivo")
    except PermissionError:
        print(f"Erro : permissão de acesso ao arquivo {nome_arquivo}")
    except Exception as e:
        print(f"Erro inesperado no arquivo '{nome_arquivo}': {e}")


### verificar se o arquivo existe, senão cria o mesmo ###
def garantir_arquivo_existe(arquivov):
    if not os.path.exists(arquivov):
        open(arquivov, 'a').close()


###====== Novas funções ======= ###

### verificar se o arquivo json existe, senão cria e inicializa 
def garantir_arquivo_json_existe(nome_arquivo):
    if not os.path.exists(nome_arquivo):   
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump([], arquivo, indent=4, ensure_ascii=False) 

### verifica se o arquivo json está vazio 
def verificar_json_vazio_por_leitura(dados):
    # recebe os dados lidos do arquivo JSON
    # verifica se a variavel dados é uma lista vazia ([])
    # ou um dicionario vazio ({})
    return dados in ([], {})

# Função para ler um arquivo JSON
def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' contém dados inválidos.")
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo: {e}")
    return []

# Função para escrever no arquivo JSON
def escrever_arquivo_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")

    except json.JSONDecodeError:
            print(f"Erro: O arquivo '{nome_arquivo}' contém dados inválidos.")       
    except Exception as e:
            print(f"Erro ao salvar os dados: {e}")
