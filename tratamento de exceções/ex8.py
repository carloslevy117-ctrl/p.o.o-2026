print("Abrindo arquivo...")

try:
    resultado = 1 / 0
except ZeroDivisionError:
    print("Ocorreu um erro.")
finally:
    print("Fechando arquivo...")