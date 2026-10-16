try:
    # Código Perigoso!
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    
except ValueError:
    # Executa apenas se o usuário digitar letras no lugar de números
    print("Por favor, digite um número válido!")
    
except ZeroDivisionError:
    # Executa apenas se o usuário digitar 0
    print("Não é possível dividir cem por zero!")
    
else:
    # O Bloco Else só executa se o Try foi 100% SUCESSO (nenhum erro aconteceu)
    print(f"O resultado com sucesso é {resultado}")
    
finally:
    # O bloco Finally sempre executa, não importa o que aconteceu (com erro ou sem erro).
    # Muito usado para fechar banco de dados e arquivos
    print("Operação finalizada.")
