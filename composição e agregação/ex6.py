class Comodo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho


class Casa:
    def __init__(self):
        self.comodos = []  # lista de cômodos

    def adicionar_comodo(self, nome, tamanho):
        comodo = Comodo(nome, tamanho)  # composição: cria dentro da casa
        self.comodos.append(comodo)

    def listar_comodos(self):
        print("Cômodos da casa:")
        for c in self.comodos:
            print(f"- {c.nome} ({c.tamanho} m²)")


# Criando uma casa
casa = Casa()

# Adicionando cômodos
casa.adicionar_comodo("Sala", 20)
casa.adicionar_comodo("Quarto", 15)
casa.adicionar_comodo("Cozinha", 10)

# Listando cômodos
casa.listar_comodos()