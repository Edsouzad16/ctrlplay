'''
NumerosMisturados = [1,2,3,1,2,5,4,4]
NumerosArrumados = set()

for num in NumerosMisturados:
    NumerosArrumados.add(num)

print(NumerosArrumados)
'''
# --- # --- #

DDDEstados = {
    '21': 'Rio de Janeiro',
    '61': 'Brasilia',
    '11': 'São Paulo',
    '32': 'Juiz de Fora',
    '19': 'Campinas'
}

DDDInput = input('Digite um DDD:\n >')
EstadoInput = input('Digite o Estodo referente:\n >')

if DDDInput in DDDEstados:
    print('DDD Existente! O Estado referente é ' + DDDEstados[DDDInput])
else:
    print('DDD ' + DDDInput + ' não existente, adicionando ao dicionário!')
    DDDEstados[DDDInput] = EstadoInput
    print(DDDEstados)
