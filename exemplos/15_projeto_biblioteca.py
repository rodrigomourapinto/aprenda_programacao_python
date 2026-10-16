class Biblioteca:
    def __init__(self, lista_livros, nome_biblioteca):
        self.livros = lista_livros
        self.nome = nome_biblioteca
        self.livros_emprestados = {}  # {livro: usuario}

    def exibir_livros(self):
        print(f"\nLivros na {self.nome}:")
        for livro in self.livros:
            print(f"- {livro}")

    def emprestar_livro(self, livro, usuario):
        if livro in self.livros:
            self.livros.remove(livro)
            self.livros_emprestados[livro] = usuario
            print(f"Livro '{livro}' emprestado a {usuario} com sucesso!")
        elif livro in self.livros_emprestados:
            print(f"Desculpe, o livro já está com {self.livros_emprestados[livro]}")
        else:
            print("Livro inexistente.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            del self.livros_emprestados[livro]
            self.livros.append(livro)
            print(f"Livro '{livro}' devolvido à biblioteca!")

if __name__ == "__main__":
    lista_inicial = ["Harry Potter", "Senhor dos Anéis", "1984", "Pequeno Príncipe"]
    bib_central = Biblioteca(lista_inicial, "Biblioteca Central Python")

    while True:
        print(f"\n--- Bem-vindo à {bib_central.nome} ---")
        print("1. Ver livros disponíveis")
        print("2. Emprestar livro")
        print("3. Devolver livro")
        print("4. Sair")
        escolha = input("Opção: ")

        if escolha == '1':
            bib_central.exibir_livros()
        elif escolha == '2':
            livro = input("Nome do livro: ")
            nome = input("Seu nome: ")
            bib_central.emprestar_livro(livro, nome)
        elif escolha == '3':
            livro = input("Nome do livro para devolver: ")
            bib_central.devolver_livro(livro)
        elif escolha == '4':
            print("Obrigado por usar o sistema!")
            break
        else:
            print("Opção Inválida.")
