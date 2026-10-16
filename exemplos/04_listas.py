minha_lista = []
numeros = [1, 2, 3, 4, 5]
mista = ["Texto", 42, 3.14, True, [1, 2]] 

frutas = ["Maçã", "Banana", "Cereja", "Laranja", "Kiwi"]
print(frutas[1])     # Retorna 'Banana'
print(frutas[1:3])   # Retorna ['Banana', 'Cereja']

frutas[0] = "Abacaxi"
tem_banana = "Banana" in frutas 

for fruta in frutas:
    print(f"Eu gosto de {fruta}")

frutas.append("Pera")
frutas.sort()
print(frutas)
