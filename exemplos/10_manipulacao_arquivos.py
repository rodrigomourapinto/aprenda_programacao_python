# Modo Write
with open("log.txt", "w") as f:
    f.write("Primeira linha de log.\n")

# Modo Append (Adiciona na linha de baixo)
with open("log.txt", "a") as f:
    f.write("Segunda linha adicionada depois!\n")

# Abre o arquivo em modo leitura
with open("log.txt", "r") as arquivo:
    conteudo = arquivo.read()       # Lê o arquivo inteiro como uma String gigante
    print("Conteúdo LIDO do arquivo:")
    print(conteudo)
