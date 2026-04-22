from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass



class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


formas = [
    Circulo(3),
    Retangulo(4, 5),
    Triangulo(6, 2)
]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")