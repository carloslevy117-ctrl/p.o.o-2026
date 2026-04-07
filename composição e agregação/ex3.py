class Autor:
    def __init__(self, nome):
        self.nome = nome


class Livro:
    def __init__(self, titulo, nome_autor):
        self.titulo = titulo
        self.autor = Autor(nome_autor)  # composição: cria o autor dentro do livro

    def mostrar_detalhes(self):
        print(f"Livro: {self.titulo}")
        print(f"Autor: {self.autor.nome}")


# Criando um objeto Livro com seu Autor
livro = Livro("Dom Casmurro", "Machado de Assis")
livro.mostrar_detalhes()