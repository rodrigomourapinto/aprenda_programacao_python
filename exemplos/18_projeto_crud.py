import tkinter as tk
from tkinter import messagebox

# Este é um esqueleto da interface CRUD sem o MySQL conectado ativamente 
# para rodar livremente em qualquer computador.

def inserir():
    nome = entrada_nome.get()
    preco = entrada_preco.get()
    
    if nome and preco:
        messagebox.showinfo("Sucesso", f"Produto '{nome}' inserido com preço de R${preco} (Simulação MySQL)")
        entrada_nome.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

janela = tk.Tk()
janela.title("Painel CRUD de Estoque")
janela.geometry("400x250")

tk.Label(janela, text="Nome do Produto:").pack(pady=5)
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack()

tk.Label(janela, text="Preço:").pack(pady=5)
entrada_preco = tk.Entry(janela, width=30)
entrada_preco.pack()

tk.Button(janela, text="Salvar no Banco", command=inserir, bg="green", fg="white").pack(pady=15)
tk.Button(janela, text="Mostrar Todos", command=lambda: messagebox.showinfo("Fetch", "Listagem simulada!")).pack()

janela.mainloop()
