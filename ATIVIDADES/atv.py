# 4 - converta metros para centímetros
def metros_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

# 5 - calcule a media de 3 notas
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# 6 - verifique se um número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
# 7 - calcule o IMC (Índice de Massa Corporal)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# 8 - peça um numer e diga se é positivo, negativo ou zero
def verificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"
    
# 9 - peça dois numeros e diga qual e maior
def numero_maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# 10 - verifique se o usuario pode votar ( idade maior que 16 )
def teste_pode_votar(idade):
    if idade < 16:
        return 'nao pode votar'
    else:
        return 'pode votar'

# 11 - faça um programa que simule um login ( usuario e senha pre definidas)
def simular_login(usuario_input, senha_input):
    usuario_predefinido = "admin"
    senha_predefinida = "1234"
    
    if usuario_input == usuario_predefinido and senha_input == senha_predefinida:
        return "Login bem-sucedido"
    else:
        return "Login falhou"

# 12 - exiba numeros de 1 a 100
def exibir_numeros():
    numeros = []
    for n in range(1, 101):
        numeros.append(n)
    return numeros

# 13 - some numeros de 1 a 100
def soma_numeros_range():
    numeros = list(range(1, 100))
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# 14 - monte uma tabua da a partir de um numero escolhido pelo usuario
def tabuada(numero):
    return numero * 1
    return numero * 2
    return numero * 3
    return numero * 4
    return numero * 5
    return numero * 6
    return numero * 7
    return numero * 8
    return numero * 9
    return numero * 10

# 15 - peça numeros até o usuario digitar 0 e exiba o total
def soma_ate_zero():
    total = 0
    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        total += numero
    return total


print('metros para ccentimetros',metros_para_centimetros(1))
print('calcular media',calcular_media(50,70,45))
print('par ou impar',verificar_par_ou_impar(7))
print('par ou impar',verificar_par_ou_impar(4))
print('calcular IMC',calcular_imc(50,35))
print('verificar numero',verificar_numero(-2))
print('verificar numero',verificar_numero(0))
print('verificar numero',verificar_numero(4))
print('numero maior',numero_maior(5,7))
print('numero maior',numero_maior(9,7))
print('teste pode votar',teste_pode_votar(17))
print('teste pode votar',teste_pode_votar(10))
print('programa login',simular_login('admin','1234'))
print('programa login',simular_login('adimon','1234'))
print('numeros 1 à 100',exibir_numeros())
print('soma numeros 1 à 100',soma_numeros_range())
print('tabuada',tabuada(2))
print('tabuada',tabuada(5))
print('soma ate zero',soma_ate_zero())