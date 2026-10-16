# 17. GUI

Programas no terminal de texto, como os que criamos até agora, funcionam muito bem para nós, programadores. Mas um usuário comum espera janelas clicáveis, botões visuais e cores.

## 1. Introdução
GUI significa *Graphical User Interface* (Interface Gráfica do Usuário). Em Python, criar janelas é surpreendentemente fácil graças às bibliotecas embutidas que abstraem os elementos visuais complexos.

## 2. Tkinter
A biblioteca padrão e mais famosa para GUIs em Python é o **Tkinter**. Ela vem instalada junto com o próprio Python, o que a torna a escolha perfeita para começar.

## 3. Introdução aos Widgets
Tudo numa interface gráfica é um "Widget" (um componente).
- Um botão é um widget.
- Uma caixa de texto para digitar a senha é um widget.
- O rótulo estático escrito "Bem-vindo" é um widget.
- A própria Janela principal é o Widget mestre (root).

## 4. Primeira GUI
Para criar a sua primeira janela, você importa o tkinter, inicializa o objeto raiz (root) e chama a função `mainloop()`. O `mainloop()` é um laço infinito mágico que mantém a janela aberta até o usuário clicar no botão vermelho "X" de fechar.

```python
import tkinter as tk

# Inicializa a janela Mestre
janela_mestre = tk.Tk()

# Altera o título da janela
janela_mestre.title("Meu Primeiro Programa Visual")

# Mantém a janela viva na tela
janela_mestre.mainloop()
```

## 5. Geometria da GUI
Para evitar que a janela nasça "espremida" num cantinho da tela, nós usamos o método `geometry()` para definir a largura e altura em pixels.

```python
janela_mestre.geometry("400x300") # 400 pixels de largura por 300 de altura
```

## 6. Trabalhando com Widgets - Parte 1
Para colocar algo dentro da janela, nós instanciamos o objeto Widget dizendo quem é o "pai" dele (a `janela_mestre`), e depois usamos o comando `.pack()` para pedir que o Tkinter encaixe aquele widget na tela de forma automática.

```python
import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")

# Criando um Rótulo de texto (Label) e colando na janela
meu_texto = tk.Label(janela, text="Olá, mundo visual!")
meu_texto.pack()

# Criando um Botão e colando na janela
meu_botao = tk.Button(janela, text="Clique Aqui")
meu_botao.pack()

janela.mainloop()
```

Nos próximos módulos veremos como conectar esses botões a funções reais!

---
*Próximo Módulo:* [[18. Projeto Três - CRUD|18_Projeto_Tres_CRUD]]
