class Nadador:
    def mover(self):
        print("Nadando...")


class Corredor:
    def mover(self):
        print("Correndo...")


class Triatleta(Nadador, Corredor):
    def mover(self):
        print("Triatleta em ação:")
        Nadador.mover(self)
        Corredor.mover(self)


# Teste
t = Triatleta()
t.mover()