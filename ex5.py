class Produto:

    def __init__(self, nome, preco, quantidade_em_estoque):

        self.__nome = nome

        self.__preco = preco

        self.__quantidade_em_estoque = quantidade_em_estoque

    def vender(self, quantidade):

        if 0 < quantidade <= self.__quantidade_em_estoque:

            self.__quantidade_em_estoque -= quantidade

            print(f"Venda de {quantidade} {self.__nome}(s) realizada.")

        else:

            print(f"Estoque insuficiente para vender {quantidade} {self.__nome}(s).")

    def repor_estoque(self, quantidade):

        if quantidade > 0:

            self.__quantidade_em_estoque += quantidade

            print(f"Reposição de {quantidade} {self.__nome}(s) realizada.")

        else:

            print("Quantidade de reposição inválida.")

    def get_nome(self):

        return self.__nome

    @property

    def preco(self):

        return self.__preco

    @preco.setter

    def preco(self, novo_preco):

        if novo_preco >= 0:

            self.__preco = novo_preco

        else:

            print("Preço não pode ser negativo.")

    @property

    def quantidade_em_estoque(self):

        return self.__quantidade_em_estoque

    @quantidade_em_estoque.setter

    def quantidade_em_estoque(self, nova_quantidade):

        if nova_quantidade >= 0:

            self.__quantidade_em_estoque = nova_quantidade

        else:

            print("Quantidade em estoque não pode ser negativa.")

    # Mantendo os métodos get para compatibilidade com o esqueleto original
   

  

    def get_quantidade_em_estoque(self):

        return self.__quantidade_em_estoque

# Exemplo de uso:

meu_produto = Produto("Notebook", 3500.00, 10)

print(f"Produto: {meu_produto.get_nome()}, Preço: R${meu_produto.preco:.2f}, Estoque: {meu_produto.quantidade_em_estoque}")

meu_produto.vender(3)

meu_produto.repor_estoque(5)

print(f"Estoque atual: {meu_produto.quantidade_em_estoque}")

meu_produto.vender(15) # Tentativa de vender mais do que há em estoque

meu_produto.preco = 3200.00 # Usando o setter property

print(f"Novo preço: R${meu_produto.preco:.2f}")
