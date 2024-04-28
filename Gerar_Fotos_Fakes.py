import os
import requests

# URL da imagem
image_url = "https://thispersondoesnotexist.com/"

# Especificando o caminho completo do diretório de destino
pasta_destino = r"C:\Users\allan\OneDrive\Imagens\fotos fakes"

while True:
    fim = input("Digite quantas fotos você vai querer: ")
    if fim.strip() == "":
        print("Por favor, digite um número.")
    elif not fim.isdigit():
        print("Por favor, digite apenas números.")
    else:
        break

quantidade_fotos = int(fim)

print("Iniciando bot")
print(f"Baixando {quantidade_fotos} aguarde...")

# Variável de contagem para o nome do arquivo
contador = 1
contador_foto = 1

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
    
    # Incrementando o contador para o próximo número
    contador_foto += 1

    if contador_foto > quantidade_fotos:
        print(f"Foram baixadas {quantidade_fotos} fotos.")
        break

