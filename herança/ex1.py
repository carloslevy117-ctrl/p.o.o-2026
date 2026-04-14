# Classe base
class Computador:
    def __init__(self, processador: str, memoria: int):
        self.processador = processador
        self.memoria = memoria


# Classe Laptop que herda de Computador
class Laptop(Computador):
    def __init__(self, processador: str, memoria: int, bateria_watts: int = 0):
        super().__init__(processador, memoria)
        self.bateria_watts = bateria_watts


# Classe Desktop que herda de Computador
class Desktop(Computador):
    def __init__(self, processador: str, memoria: int, gabinete: str = ""):
        super().__init__(processador, memoria)
        self.gabinete = gabinete


# Exemplos de uso
laptop = Laptop("Intel i7", 16, 60)
desktop = Desktop("AMD Ryzen 5", 32, "ATX")

print(vars(laptop))
print(vars(desktop))