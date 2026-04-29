class Veiculo:
    def acelerar(self):
        print("Acelerando...")


class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando 🚗")


class Moto(Veiculo):
    def acelerar(self):
        print("Moto acelerando 🏍️")


# Lista de veículos (polimorfismo)
veiculos = [Carro(), Moto()]

for v in veiculos:
    v.acelerar()
