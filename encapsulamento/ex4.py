class ContaBancariaComProperty:


   def __init__(self, saldo_inicial):


       self.__saldo = saldo_inicial


   @property


   def saldo(self):


       """Este é o getter para o saldo."""


       return self.__saldo


   @saldo.setter


   def saldo(self, novo_saldo):


       """Este é o setter para o saldo."""


       if novo_saldo >= 0:


           self.__saldo = novo_saldo


       else:


           print("Saldo não pode ser negativo.")


# Uso da classe com property


conta_prop = ContaBancariaComProperty(2000)


print(f'Saldo inicial (property): R${conta_prop.saldo:.2f}')


conta_prop.saldo = 2500 # Usando o setter


print(f'Novo saldo (property): R${conta_prop.saldo:.2f}')


conta_prop.saldo = -50 # Tentando definir um saldo negativo


print(f'Saldo final (property): R${conta_prop.saldo:.2f}')