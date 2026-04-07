class Professor:
    def __init__(self, nome, titulacao):
        self.nome = nome
        self.titulacao = titulacao


class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor  # recebe um professor já criado

    def exibir_info(self):
        print(f"Disciplina: {self.nome}")
        print(f"Professor: {self.professor.nome}")
        print(f"Titulação: {self.professor.titulacao}")


# Criando um professor
prof = Professor("Carlos Levy", "Doutor")

# Associando o professor a uma disciplina
disciplina = Disciplina("Programação", prof)

# Exibindo informações
disciplina.exibir_info()
