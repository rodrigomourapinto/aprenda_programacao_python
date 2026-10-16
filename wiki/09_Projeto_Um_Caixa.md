# 9. Projeto Um - Caixa de Supermercado

Chegou a hora de juntar todo o conhecimento sobre Variáveis, Tipos de Dados, Dicionários, Laços, Condicionais e Funções para criar nosso primeiro software real!

## 1. Introdução
Neste módulo, vamos criar um sistema simples de Caixa (PDV) de supermercado, simulando as operações diárias de um caixa registrador.

## 2. Sobre o que é o projeto?
O projeto consiste em um programa no terminal onde o usuário ("o caixa") digita os códigos dos produtos e as quantidades compradas por um cliente. O programa deverá calcular o total, aplicar descontos aplicáveis e exibir o "recibo" ou fatura final da compra.

## 3. Inserindo Produtos
A melhor forma de armazenar nossos produtos em um supermercado simulado é usando **Dicionários**, onde a *chave* é o ID do produto e o *valor* é o preço.

```python
# Nosso pequeno banco de dados em memória
estoque_precos = {
    "101": 5.50,  # Leite
    "102": 3.20,  # Pão
    "103": 8.90,  # Queijo
}
```

## 4. Calculando Preço
Precisaremos de um Laço `while` para manter o caixa aberto até que o atendente digite `0` (sinalizando o fim da compra).

```python
carrinho = []

while True:
    codigo = input("Digite o código do produto (ou 0 para finalizar): ")
    if codigo == '0':
        break
    
    if codigo in estoque_precos:
        qtd = int(input("Digite a quantidade: "))
        preco_unitario = estoque_precos[codigo]
        subtotal = preco_unitario * qtd
        carrinho.append({"codigo": codigo, "qtd": qtd, "subtotal": subtotal})
    else:
        print("Produto não encontrado!")
```

## 5. Calculando Desconto
Vamos criar uma função que verifica o valor final e aplica um desconto especial. Se a compra for acima de 50 reais, daremos 10% de desconto.

```python
def aplicar_desconto(total):
    if total > 50:
        return total * 0.90 # Aplica 10% de desconto
    return total
```

## 6. Fazendo a Conta
A conta final é calculada iterando sobre todos os subtotais salvos no nosso carrinho (Lista de Dicionários).

```python
soma_total = 0
for item in carrinho:
    soma_total += item["subtotal"]

total_com_desconto = aplicar_desconto(soma_total)
```

## 7. Texto Padrão
Para o recibo final, vamos formatar a string de saída usando f-strings para que fique com uma cara profissional de nota fiscal.

## 8. Código Final e Execução

Abaixo está o nosso script completo reunindo tudo o que discutimos:

```python
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
```

## 9. Para Concluir
Parabéns! Você acabou de construir um programa modular e coerente usando toda a base fundamental da linguagem Python. A partir daqui, as aplicações só ficam mais robustas.

---
*Próximo Módulo:* [[10. Manipulação de Arquivos|10_Manipulacao_de_Arquivos]]
