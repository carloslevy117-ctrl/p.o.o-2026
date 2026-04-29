frase = input("Digite uma frase: ").lower()

for p in ".,!?":
    frase = frase.replace(p, "")

palavras = frase.split()

unicas = set(palavras)

frequencia = {}
for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("\nPalavras únicas:")
for palavra in sorted(unicas):
    print(palavra)

print("\nFrequência das palavras:")
for palavra in sorted(frequencia):
    print(f"{palavra}: {frequencia[palavra]}")