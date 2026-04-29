# Classe base Motor
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar_motor(self):
        print("Motor ligado")

    def exibir_info(self):
        print(f"Potência: {self.potencia} CV")


# Classe Eletrico
class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria

    def carregar(self):
        print("Carregando bateria...")

    def exibir_info(self):
        print(f"Bateria: {self.bateria} kWh")


# Classe Combustao
class Combustao:
    def __init__(self, tanque):
        self.tanque = tanque

    def abastecer(self):
        print("Abastecendo tanque...")

    def exibir_info(self):
        print(f"Tanque: {self.tanque} L")


# Carro Elétrico (Motor + Eletrico)
class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia, bateria):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)

    def exibir_info(self):
        print("=== Carro Elétrico ===")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)


# Carro Híbrido (Motor + Eletrico + Combustao)
class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia, bateria, tanque):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)
        Combustao.__init__(self, tanque)

    def exibir_info(self):
        print("=== Carro Híbrido ===")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
        Combustao.exibir_info(self)


# Teste
carro_eletrico = CarroEletrico(150, 75)
carro_hibrido = CarroHibrido(200, 50, 45)

carro_eletrico.exibir_info()
print()
carro_hibrido.exibir_info()