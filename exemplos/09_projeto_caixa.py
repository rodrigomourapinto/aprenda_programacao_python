def aplicar_desconto(total):
    if total > 50:
        print("--- Desconto de 10% Aplicado! ---")
        return total * 0.90
    return total

estoque = {"101": 5.50, "102": 3.20, "103": 8.90}
carrinho = []

print("=== SISTEMA DE CAIXA ===")
while True:
    codigo = input("Código do produto (0 para sair): ")
    if codigo == '0':
        break
    
    if codigo in estoque:
        qtd = int(input("Quantidade: "))
        carrinho.append(estoque[codigo] * qtd)
    else:
        print("Produto inválido.")

soma_bruta = sum(carrinho)
valor_final = aplicar_desconto(soma_bruta)

print(f"\n--- RECIBO FINAL ---")
print(f"Total Bruto: R$ {soma_bruta:.2f}")
print(f"Total a Pagar: R$ {valor_final:.2f}")
print("======================\n")
