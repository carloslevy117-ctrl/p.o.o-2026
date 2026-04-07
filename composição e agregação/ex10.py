# Classe Aluno
class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


# Classe Turma
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Agregação: alunos podem existir fora da turma

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        if not self.alunos:
            return "Nenhum aluno nesta turma."
        return ", ".join([aluno.nome for aluno in self.alunos])


# Classe Escola
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []  # Composição: escola possui turmas

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def listar_turmas(self):
        if not self.turmas:
            print("Não há turmas cadastradas na escola.")
        else:
            print(f"Escola {self.nome} possui as seguintes turmas e alunos:")
            for turma in self.turmas:
                print(f"Turma: {turma.nome} | Alunos: {turma.listar_alunos()}")


# --- Exemplo de uso ---
if __name__ == "__main__":
    # Criando escola
    escola = Escola("Escola Modelo")

    # Criando turmas
    turma1 = Turma("1º Ano")
    turma2 = Turma("2º Ano")

    # Adicionando turmas à escola
    escola.adicionar_turma(turma1)
    escola.adicionar_turma(turma2)

    # Criando alunos
    aluno1 = Aluno("Alice")
    aluno2 = Aluno("Bruno")
    aluno3 = Aluno("Carla")

    # Adicionando alunos às turmas
    turma1.adicionar_aluno(aluno1)
    turma1.adicionar_aluno(aluno2)
    turma2.adicionar_aluno(aluno3)

    # Exibindo turmas e alunos
    escola.listar_turmas()