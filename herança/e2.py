# Classe base
class Animal:
    def __init__(self):
        self.grupo = ""  # atributo público


# Classe Cachorro que herda de Animal
class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.grupo = "mamífero"


# Exemplo de uso
cachorro = Cachorro()
print(cachorro.grupo)  # saída: mamífero