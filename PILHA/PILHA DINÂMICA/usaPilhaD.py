import PilhaD
p = PilhaD.PilhaD()

frase = input("Digite uma frase: ")
resultado = []

for palavra in frase.split():

    for letra in palavra:
        p.push(letra)

    invertida = ""
    while not p.esta_vazia():
        invertida += p.ver_topo()
        p.pop()

    resultado.append(invertida)

print("Frase original:", frase)
print("Saída:", " ".join(resultado))