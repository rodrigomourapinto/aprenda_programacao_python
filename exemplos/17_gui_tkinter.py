import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Meu Primeiro Programa Visual")

# Criando um Rótulo de texto (Label) e colando na janela
meu_texto = tk.Label(janela, text="Olá, mundo visual!")
meu_texto.pack(pady=20)

# Criando um Botão e colando na janela
meu_botao = tk.Button(janela, text="Clique Aqui", command=lambda: print("Botão foi clicado!"))
meu_botao.pack()

janela.mainloop()
