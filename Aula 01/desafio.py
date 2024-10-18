texto = "paralelepipedo"
vogais = ["a", "e", "i", "o", "u"]
contagemVogais = {}

for letra in texto:
    print(letra)
    if letra in vogais:
        if letra in contagemVogais:
            contagemVogais[letra] += 1
        else:
            contagemVogais[letra] = 1

# print("Quantidade total de vogais:", sum(contagemVogais.values()))
# print("Quantidade de cada vogal:", contagemVogais)
