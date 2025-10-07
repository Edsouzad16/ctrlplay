# criando um função
def nomefuncao() :
    # codigo
    pass # evita um erro;

# chamando uma função
nomefuncao()

# somando

def somar(a,b) :
    print(a + b)

somar(23, 30)

# funçoes que retornam valores
# para retornar um valor usamos a palavra reservada: return.

def diminuir(a,b):
    total = a-b
    return total

resultado = diminuir(5,2)
print(resultado)

# funcoes recursivas

def DobraLencol(lencol, gaveta):
    if lencol < gaveta:
        return 0
    else:
        DobraLencol= lencol / 2