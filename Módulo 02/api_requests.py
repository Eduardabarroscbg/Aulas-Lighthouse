# Módulo 2 - Bibliotecas e consumindo uma API
# Biblioteca é um código que alguém já escreveu pra resolver um problema comum,
# e que dá pra importar em vez de reinventar a roda.
#
# Analogia da aula: pensa num restaurante. O front-end é o cliente, o back-end
# é a cozinha, e a API é o garçom - o intermediário que busca a informação lá
# atrás e traz pra gente, sem expor os dados diretamente.
#
# O retorno de uma API geralmente vem em JSON, que segue a mesma lógica de
# dicionário + lista que a gente já usa em Python.

import requests

response = requests.get("https://dummyjson.com/users")
dados = response.json()

usuarios_lista = dados["users"]

for i in range(len(usuarios_lista)):
    usuario = usuarios_lista[i]
    print(f"{usuario['firstName']} {usuario['lastName']}")

    if usuario["age"] >= 30:
        print("Essa pessoa tem mais de 30 anos")
    else:
        print("Essa pessoa tem menos de 30 anos")

# Erros e try/except: pra evitar que um erro quebre o programa inteiro
try:
    numero = int(input("Digite um número inteiro: "))
except:
    print("Valor inválido, digite um número inteiro")
