class Animal:
    def emitir_som(self):
        return "Algum som genérico"


class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"


class Gato(Animal):
    def emitir_som(self):
        som_original = super().emitir_som() 
        print(som_original)  
        return "Miado"



animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.emitir_som())