#  def soma_numeros_range():
#      numeros = [range(1, 100)]
#      for numero in numeros:
#          soma = (numeros)
#      return soma

def soma_numeros_range():
    numeros = list(range(1, 100))
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(soma_numeros_range())