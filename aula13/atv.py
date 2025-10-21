class Banco:
    def __init__(self,Consultar_saldo,Alterar_titular):
        self.Consultar_saldo
        self.Alterar_titular

    saldo = 86

    def Depositar(self):
        ValDep = int(input('Quanto depositar?\n>>'))
        int(self.saldo + ValDep)

    def Sacar(self):
        ValSac = int(input('Quanto sacar?\n>>'))
        self.saldo - ValSac

    def Saldo(self):
        print(int(self.saldo))

