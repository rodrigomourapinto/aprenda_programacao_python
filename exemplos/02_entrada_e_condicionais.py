# Solicitando o nome do usuário
nome = input("Qual é o seu nome? ")
# Exibindo uma saudação
print("Olá,", nome)

idade = int(input("Qual sua idade? "))

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")
