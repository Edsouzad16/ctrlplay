class Ventilador:
    Marca = 'Ventisol'
    Cor = 'Preto'
    Pas = 6
    Tipo = 'Silencioso'

    def Ligar(self):
        print('Ventilador ligado!!')

    def Desligar(self):
        print('Ventilador desligado!!')

MeuVentilador = Ventilador()

# MeuVentilador.Ligar()
# MeuVentilador.Desligar()