# tupla - uma lista que nao pode ser alterada

numeros = (1, 2, 3, 4, 5)

# set() - lista de elementos unicos

numbers = set()

# adicionando ao set()

numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(1)
# {1, 2, 3}

# dicionarios
# estrutura que armazena uma chave e um valor

pessoa = {
    'nome': 'Edson',
    'idade': 14,
    'altura': 1.65
}
# adicionando ao dicionario

pessoa['idiomas'] = 'Português', 'Inglês'

carro = {
    'Marca': 'Toyota'
}
'''
print(carro)

NovaChave = input('O que você gostaria de adicionar ao carro? \n -')
NovoValor = input('Qual seria o valor? \n -')

carro[NovaChave] = NovoValor

print(carro)
'''
# Dicionarios - keys(), values() e items()

# keys() - retorna as chaves
# values() - retorna os valores
# Items() - retorna tudo como tuplas
livro = set()
livro.keys()
