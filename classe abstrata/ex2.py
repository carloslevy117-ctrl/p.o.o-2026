from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carregavel(ABC):
    @abstractmethod
    def carregar(self):
        pass

class Smartphone(DispositivoEletronico, Carregavel):
    def ligar(self):
        print("Smartphone ligado")

    def desligar(self):
        print("Smartphone desligado")

    def carregar(self):
        print("Smartphone carregando")

class Notebook(DispositivoEletronico, Carregavel):
    def ligar(self):
        print("Notebook ligado")

    def desligar(self):
        print("Notebook desligado")

    def carregar(self):
        print("Notebook carregando")

class FoneDeOuvido(DispositivoEletronico):
    def ligar(self):
        print("Fone de ouvido ligado")

    def desligar(self):
        print("Fone de ouvido desligado")

dispositivos = [Smartphone(), Notebook(), FoneDeOuvido()]
carregaveis = [Smartphone(), Notebook()]

for d in dispositivos:
    d.ligar()
    d.desligar()

for c in carregaveis:
    c.carregar()