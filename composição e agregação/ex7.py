class Processador:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade


class Memoria:
    def __init__(self, capacidade):
        self.capacidade = capacidade


class Computador:
    def __init__(self, modelo_proc, velocidade_proc, capacidade_mem):
        # composição: criando tudo dentro do computador
        self.processador = Processador(modelo_proc, velocidade_proc)
        self.memoria = Memoria(capacidade_mem)

    def exibir_configuracao(self):
        print("Configuração do computador:")
        print(f"Processador: {self.processador.modelo}")
        print(f"Velocidade: {self.processador.velocidade} GHz")
        print(f"Memória: {self.memoria.capacidade} GB")


# Criando um computador
pc = Computador("Intel i5", 3.2, 64)

# Exibindo configuração
pc.exibir_configuracao()