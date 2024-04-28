import ctypes
import os
import requests

ctypes.windll.kernel32.SetConsoleTitleW(f"Gerar Fotos Fakes")
# URL da imagem
image_url = "https://thispersondoesnotexist.com/"

# Obtendo o diretório padrão de imagens do sistema operacional
pasta_destino = os.path.join(os.path.expanduser('~'), 'Downloads')

# Verificando se o diretório existe e, se não, criando-o
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

print("Iniciando bot")


print("Caminho da pasta onde vai ficar salvas as fotos fakes:",pasta_destino)

def baixar_fotos():
    while True:
        fim = input("Digite quantas fotos você vai querer: ")
        if fim.strip() == "":
            print("Por favor, digite um número.")
        elif not fim.isdigit():
            print("Por favor, digite apenas números.")
        else:
            break

    quantidade_fotos = int(fim)
    print(f"Baixando {quantidade_fotos} aguarde...")

    # Variável de contagem para o nome do arquivo
    contador = 1
    contadorn = 1

    while True:
        # Criando o nome do arquivo com o número atual
        nome_arquivo = f"imagem_{contador}.jpg"
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)

        # Verificando se o arquivo já existe
        if os.path.exists(caminho_completo):
            contador += 1
            continue

        # Salvando a imagem
        response = requests.get(image_url)

        with open(caminho_completo, "wb") as f:
            f.write(response.content)   

        ctypes.windll.kernel32.SetConsoleTitleW(f"Gerar Fotos Fakes: {contadorn}")
        contadorn += 1
        

        if contadorn > quantidade_fotos:
            print(f"Foram baixadas {quantidade_fotos} fotos.")
            break

    while True:
        opcao = input("Deseja gerar mais fotos? (s/n): ")
        if opcao.lower() not in ['s', 'n']:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
        else:
            return opcao.lower() == 's'
            

while baixar_fotos():
    print("-" * 40)

