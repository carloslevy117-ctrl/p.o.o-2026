class Animal:
    def emitir_som(self):
        return "Algum som genérico"


class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"


class Gato(Animal):
    def emitir_som(self):
        return "Miado"


animais = [Animal(), Cachorro(), Gato(), Cachorro()]

for animal in animais:
    print(animal.emitir_som())