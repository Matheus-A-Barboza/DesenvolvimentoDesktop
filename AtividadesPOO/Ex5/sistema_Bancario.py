class conta_bancaria():
    def __init__(self, numero : int, titular, saldo : float):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposito(self, depositar):
        self.saldo += depositar

    def mostrar_conta(self):
        print(f'Numero da conta: {self.numero}\n'
              f'Titular da Conta: {self.titular}\n'
              f'Saldo total: R${self.saldo}')

conta = conta_bancaria(99999, 'Matheus', 80000)
conta.mostrar_conta()
