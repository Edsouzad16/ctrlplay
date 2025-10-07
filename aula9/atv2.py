def CalculadoraKelvin (a):
    return a + 273

def CalculadoraFahren (a):
    return a * 1.8 + 32

ConTip = input('Escolha a temperatura que quer converter: \n Celcius para Kelvin \n Celcius para Fahrenheit \n')
if ConTip == 'Celcius para Kelvin \n':
    ConNum = int(input('Qual valor quer converter? \n'))
    print(CalculadoraFahren(ConNum))