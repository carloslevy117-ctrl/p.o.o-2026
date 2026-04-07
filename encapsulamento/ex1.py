class Estudante:
    def __init__(self, id, nome):
        self._id = id          # protegido (não pode ser alterado depois)
        self.nome = nome
        self.__creditos = 1    # privado, valor padrão

    # Propriedade para acessar o id (somente leitura)
    @property
    def id(self):
        return self._id

    # Getter de créditos
    @property
    def creditos(self):
        return self.__creditos

    # Setter de créditos com validação
    @creditos.setter
    def creditos(self, valor):
        if valor > 0:
            self.__creditos = valor
        else:
            print("Valor inválido! Créditos definidos como 1.")
            self.__creditos = 1

    # Método para mostrar os dados
    def detalhar(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Créditos: {self.creditos}")
        print("-" * 20)


# TESTE
estudante1 = Estudante(1, "girassol")
estudante2 = Estudante(2, "Levy")

# Modificando créditos
estudante1.creditos = 8
estudante2.creditos = 10  # inválido, vira 1

# Exibindo dados
estudante1.detalhar()
estudante2.detalhar()