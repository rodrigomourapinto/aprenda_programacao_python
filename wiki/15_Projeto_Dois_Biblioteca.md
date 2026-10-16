# 15. Projeto Dois - Aplicativo de Gerenciamento de Biblioteca

Com a base firme em OOP (Programação Orientada a Objetos), faremos agora o nosso segundo projeto, muito mais organizado e real do que o script de Caixa anterior.

## 1. Introdução
Nosso objetivo é desenvolver um programa de terminal para administrar uma biblioteca, usando Classes para separar as responsabilidades e lidar com o empréstimo e devolução de livros.

## 2. Sobre o que é o projeto?
O sistema permitirá gerenciar o acervo da biblioteca:
- Ver livros disponíveis
- Emprestar um livro para um usuário (removendo dos disponíveis)
- Devolver um livro
- Manter o banco de dados atualizado enquanto o programa roda.

## 3. A Classe Biblioteca
A classe será o coração do projeto. Ela deve nascer (via construtor `__init__`) já possuindo uma lista de livros e o nome da biblioteca.

```python
class Biblioteca:
    def __init__(self, lista_livros, nome_biblioteca):
        self.livros = lista_livros
        self.nome = nome_biblioteca
        self.livros_emprestados = {}  # Um dicionário guardando: {livro: usuario}
```

## 4. Adicionando Funcionalidades
Vamos adicionar os métodos dentro da Classe para executar as regras de negócio.

```python
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
```

## 5. Desenvolvendo o Menu
O menu será a interface que dialoga com o usuário humano. Diferente da Classe Biblioteca, que não usa `print()` nem `input()`, o menu cuidará apenas dessa parte visual.

## 6. Nosso Banco de Dados
Para simplificar, o "Banco de Dados" inicial será uma lista simples de Strings injetada na criação do objeto Biblioteca.

## 7. Trabalhando com o Principal
Aqui montamos o laço `while True` que constrói a interface textual.

## 8. Código Final e Execução

```python
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
```

## 9. Para Concluir
Neste projeto, a Lógica de Negócios (como as regras de empréstimo) ficou isolada dentro da Classe Biblioteca. Isso é um conceito fundamental de OOP: a Interface do Usuário não sabe como a Biblioteca funciona internamente, apenas usa seus botões (métodos). 

---
*Próximo Módulo:* [[16. Conectividade com Banco de Dados|16_Conectividade_com_Banco_de_Dados]]
