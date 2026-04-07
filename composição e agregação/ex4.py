class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []  # lista de jogadores

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Time: {self.nome}")
        print("Jogadores:")
        for jogador in self.jogadores:
            print(f"- {jogador.nome} ({jogador.posicao})")


# Criando jogadores
j1 = Jogador("Cristiano Ronaldo", "Atacante")
j2 = Jogador("Neymar", "Ponta")
j3 = Jogador("Messi", "Ponta")

# Criando um time
time = Time("Miami")

# Adicionando jogadores ao time
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.adicionar_jogador(j3)

# Listando jogadores
time.listar_jogadores()