# Classe base
class Forma:
    def area(self):
        return 0


# Classe Retangulo que herda de Forma
class Retangulo(Forma):
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


# Exemplo de uso
forma = Forma()
retangulo = Retangulo(5, 3)

print(forma.area())      # saída: 0
print(retangulo.area())  # saída: 15