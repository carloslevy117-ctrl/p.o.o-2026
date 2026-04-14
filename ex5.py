# Classe base
class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


# Classe Gerente
class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, bonus: float):
        super().__init__(nome, salario)
        self.bonus = bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Bônus: R$ {self.bonus:.2f}")


# Classe Desenvolvedor
class Desenvolvedor(Funcionario):
    def __init__(self, nome: str, salario: float, linguagem: str):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Linguagem: {self.linguagem}")


# Criando objetos
gerente = Gerente("Carlos", 8000, 2000)
dev = Desenvolvedor("george", 5000, "Python")

# Exibindo dados
print("=== Gerente ===")
gerente.exibir_dados()

print("\n=== Desenvolvedor ===")
dev.exibir_dados()
