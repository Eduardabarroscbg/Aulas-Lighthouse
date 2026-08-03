# Módulo 2 - Dicionários
# Diferente da lista, o dicionário guarda cada valor associado a uma chave (rótulo),
# então fica bem mais claro o que cada informação representa.

aluno = {
    "nome": "Maria",
    "nota": 10,
    "curso": "Python"
}

print(aluno["nome"])     # Maria
print(aluno.keys())      # todas as chaves
print(aluno.values())    # todos os valores

for chave, valor in aluno.items():
    print(chave, valor)
