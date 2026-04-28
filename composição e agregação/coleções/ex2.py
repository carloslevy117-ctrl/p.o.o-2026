dados = {}

while True:
    entrada = input("Digite o ano de nascimento (ou pressione Enter para sair): ")
    
    if entrada == "":
        break

    ano = int(entrada)

    if ano in dados:
        dados[ano] += 1
    else:
        dados[ano] = 1

print("\nRelatório:")
for ano in sorted(dados):
    print(f"{ano}: {dados[ano]} pessoa(s)")