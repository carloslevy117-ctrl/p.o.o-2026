class ContaBancaria:


   def __init__(self, saldo_inicial):


       self.__saldo = saldo_inicial  # Atributo privado


   def depositar(self, valor):


       if valor > 0:


           self.__saldo += valor


           print(f' Depósito de R{valor:.2f} realizado. Novo saldo: R{self.__saldo:.2f}')


       else:


           print('Valor de depósito inválido.')


   def sacar(self, valor):


       if 0 < valor <= self.__saldo:


           self.__saldo -= valor


           print(f'Saque de R${valor:.2f} realizado. Novo saldo: R${self.__saldo:.2f}')


       else:


           print('Valor de saque inválido ou saldo insuficiente.')


   def get_saldo(self):


       return self.__saldo


   def set_saldo(self, novo_saldo):


       # Exemplo de como um setter pode ser usado para validar dados


       if novo_saldo >= 0:


           self.__saldo = novo_saldo


       else:


           print('Saldo não pode ser negativo.')


# Uso da classe


minha_conta = ContaBancaria(1000)


minha_conta.depositar(500)


minha_conta.sacar(200)


print(f'Saldo atual: R${minha_conta.get_saldo():.2f}')


# Tentativa de acesso direto (desencorajado)


# print(minha_conta.__saldo) # Isso geraria um AttributeError


# print(minha_conta._ContaBancaria__saldo) # Acesso via name mangling (não recomendado)


minha_conta.set_saldo(3000)


print(f'Saldo após set_saldo: R${minha_conta.get_saldo():.2f}')


minha_conta.set_saldo(-100) # Tentativa de definir saldo negativo


print(f'Saldo final: R${minha_conta.get_saldo():.2f}')