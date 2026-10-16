def calcular_area(base, altura):
    area = base * altura
    return area

terreno_a = calcular_area(10, 5)  # Retornará 50
terreno_b = calcular_area(20, 2)  # Retornará 40

print("Terreno A:", terreno_a)
print("Terreno B:", terreno_b)

def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()
saudacao("Rodrigo")

dobrar_lambda = lambda x : x * 2
print("Lambda dobro:", dobrar_lambda(5))
