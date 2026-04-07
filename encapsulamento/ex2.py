class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saque inválido ou saldo insuficiente.")

    def consultar_saldo(self):
        return self._saldo


# TESTE
conta = ContaBancaria("carlos levy", 200)

conta.depositar(100)
conta.sacar(90)

print("Titular:", conta.titular)
print("Saldo atual:", conta.consultar_saldo())