class Cidade:
    def __init__(self, nome):
        self._nome = nome  # atributo "privado"

    @property
    def nome(self):
        return self._nome  # somente leitura


class Pessoa:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade  # objeto da classe Cidade


class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono  # objeto da classe Pessoa


# Exemplo de uso:
cidade = Cidade("Natal")
pessoa = Pessoa("Levy", cidade)
animal = Animal("Drogon", pessoa)

print(animal.nome)           
print(animal.dono.nome)     
print(animal.dono.cidade.nome)  