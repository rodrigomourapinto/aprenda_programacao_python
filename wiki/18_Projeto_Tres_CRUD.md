# 18. Projeto Três - Aplicativo CRUD

Chegamos ao ápice do aprendizado Python! Vamos combinar **Interfaces Gráficas (Tkinter)** com **Banco de Dados (MySQL)** para criar um sistema "CRUD" completo.

## 1. Introdução
CRUD é um acrônimo vital no desenvolvimento de software que significa:
- **C**reate (Criar / Inserir)
- **R**ead (Ler / Consultar)
- **U**pdate (Atualizar)
- **D**elete (Apagar)
Quase todo aplicativo do mundo (como o Instagram, um sistema de hospital, ou um site de vendas) é essencialmente um gigantesco CRUD.

## 2. Sobre o que é o projeto?
Criaremos um painel visual de gerenciamento de Estoque. Nele, teremos caixas de texto e botões para Adicionar um novo produto, Editar um existente, Apagá-lo, ou Listar tudo que existe salvo no banco de dados, aparecendo de volta na nossa interface.

## 3. Criando Banco de Dados e Tabela
Antes de tudo, precisamos do MySQL ligado e um banco criado. Suponha que já rodamos o SQL: `CREATE TABLE itens (id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(100), preco FLOAT)`.

## 4. Desenvolvendo a GUI
Nossa interface terá Labels (rótulos), Entry (campos de texto para o usuário digitar) e Buttons.

```python
import tkinter as tk
import mysql.connector

# Omissão da Conexão MySQL por brevidade...

janela = tk.Tk()
janela.title("Painel CRUD de Estoque")

tk.Label(janela, text="Nome do Produto:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Preço:").pack()
entrada_preco = tk.Entry(janela)
entrada_preco.pack()
```

## 5. Método de Inserção (Create)
Quando o botão "Salvar" for clicado, ele ativará esta função, que lê os `Entry` e envia pro MySQL.

```python
def inserir():
    # Pega o que o usuário digitou usando .get()
    nome = entrada_nome.get()
    preco = float(entrada_preco.get())
    
    cursor.execute("INSERT INTO itens (nome, preco) VALUES (%s, %s)", (nome, preco))
    conexao.commit()
    print("Sucesso!")

# Botão conectado à função usando 'command'
tk.Button(janela, text="Salvar", command=inserir).pack()
```

## 6. Método de Atualização (Update)
Similar à inserção, mas precisa pedir o ID do item que o usuário deseja mudar e rodar o SQL `UPDATE itens SET preco = %s WHERE id = %s`.

## 7. Método Fetch (Read)
A consulta busca os dados no banco (`SELECT * FROM itens`) e depois cria *Labels* dinamicamente ou preenche uma `Listbox` para exibir na tela do aplicativo.

## 8. Método Deletar (Delete)
Pede um ID na interface, e roda o SQL `DELETE FROM itens WHERE id = %s`.

## 9. Mostrar e Reiniciar
Como bônus, é vital ter um botão de "Atualizar/Limpar Tela" que limpa os formulários (`entrada_nome.delete(0, tk.END)`) e dá um "refresh" na listagem Fetch.

## 10. Código Final e Execução
Este projeto exige um cuidado profundo na união entre o front-end (Tkinter) e o back-end (MySQL). Com os blocos montados juntos, você acaba de criar um software verdadeiramente pronto para o mercado corporativo!

---
*Próximo Módulo:* [[19. Preparação para Entrevista Python|19_Preparacao_Entrevista_Python]]
