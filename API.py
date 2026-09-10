#antes de compilar e rodar o código, rodar no terminal os dois comandos:
#python3 -m venv .venv
#source .venv/bin/activate

import urllib.request
import json

cep = str(input("Digite um CEP que deseja consultar: \nR: "))

url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = (urllib.request.urlopen(url))

dados = json.loads(resposta.read())

print(dados["logradouro"])
print(dados["bairro"])
print(dados["localidade"])
print(dados["uf"])