usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com",
    "is_admin": False
}

print(usuario["nome"])  # 'João'

usuario["idade"] = 26
usuario["telefone"] = "9999-9999"
del usuario["is_admin"]

for chave, valor in usuario.items():
    print(f"O(A) {chave} do usuário é {valor}.")

endereco = usuario.get("endereco", "Não Cadastrado")
print("Endereço:", endereco)
