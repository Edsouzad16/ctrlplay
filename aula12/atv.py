# class Ventilador:
#     Marca = 'Ventisol'
#     Cor = 'Preto'
#     Pas = 6
#     Tipo = 'Silencioso'

#     def Ligar(self):
#         print('Ventilador ligado!!')

#     def Desligar(self):
#         print('Ventilador desligado!!')

# MeuVentilador = Ventilador()

# MeuVentilador.Ligar()
# MeuVentilador.Desligar()

# - - - #

class Carros:
    Cor = ''

    def __init__(self, Marca , Modelo, Ano):
        self.Marca
        self.Modelo
        self.Ano

    def Ligar():
        print('Carro ligado!!')
    
    def Desligar():
        print('Carro Desligado!!')

    def getInformacoes(self):
        info = f'Marca: {self.Marca}, Modelo: {self.Modelo}, Ano: {self.Ano}'
        return info
    
    def setCor(self, Cor):
        self.Cor = Cor

# Chamando

Carro1 = Carros('Toyota', 'AE86', 1983)