# Classe base
class Animal:
    def fazer_som(self):
        return "Som genérico"


# Classe derivada
class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"


# Teste
a = Animal()
c = Cachorro()

print(a.fazer_som())  # Som genérico
print(c.fazer_som())  # Latido