# Classe Motor
class Motor:
    def tipo(self):
        return "Motor a combustão"


# Classe Carro (usa composição)
class Carro:
    def __init__(self):
        self.motor = Motor()

    def mostrar_motor(self):
        print(self.motor.tipo())


# Classe MotorEletrico herdando de Motor
class MotorEletrico(Motor):
    def tipo(self):
        return "Motor elétrico"


# Classe CarroEletrico herdando de Carro
class CarroEletrico(Carro):
    def __init__(self):
        self.motor = MotorEletrico()


# Teste
carro = Carro()
carro.mostrar_motor()

carro_eletrico = CarroEletrico()
carro_eletrico.mostrar_motor()