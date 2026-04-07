class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligado.")


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # composição: cria o motor dentro do carro

    def ligar_carro(self):
        print(f"Ligando o {self.modelo}...")
        self.motor.ligar()


# Exemplo de uso:
carro = Carro("Lambo", 1000)
carro.ligar_carro()