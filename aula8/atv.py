NovoNome = input('Escreva um nome a ser adicionado: \n -')


with open('./aula8/nomes.txt', 'a') as NomesArquivo:
    NomesArquivo.write(NovoNome + '\n')
    print('Nome ' + NovoNome + ' adicionado!')

NomesArquivo = open('./aula8/nomes.txt', 'r')
print(NomesArquivo.read())

