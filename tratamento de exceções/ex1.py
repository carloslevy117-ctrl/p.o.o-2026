def adicionar_valor(inicial, adicional):
    if adicional <= 0:
        raise ValueError("Somente valores positivos devem ser adicionados ao valor inicial")
    return inicial + adicional

try:
    resultado = adicionar_valor(10, 5)
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")

try:
    resultado = adicionar_valor(10, -3)
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")