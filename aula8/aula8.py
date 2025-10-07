# aula 8 - arquivos

# criando arquivos

# abrindo arquivos
'''''
arquivo = open('./aula8/texto.txt')
'''''
# operações nos arquivos

# r (read only) - apenas leitura
# w (write only) - apenas escrita

# a (append) - escreve algo no final do arquivo
# r+ (read and write) - lê e escreve em um arquivo

'print(arquivo.read())'

# seek(0) - volta o ponteiro para o inicio do arquivo (índice 0)

'arquivo.seek(0)'

# readlines() - lê linhas do arquivo

'print(arquivo.readlines())'

# loop for
''
arquivo = open('./aula8/texto.txt')

for i, linha in enumerate(arquivo):
    print(f'Linha {i} - {linha}')
    ''
# escrevendo um arquivo
# write() - função usada para escrever em um arquivo
'''''
arquivo = open('./aula8/texto.txt', 'w')
arquivo.write('<Escrevendo em um arquivo>')
'''

