# 7. Conjuntos

Até agora cobrimos Listas, Tuplas e Dicionários. O quarto elemento fundamental em Estruturas de Dados do Python são os Conjuntos (Sets).

## 1. Introdução
Se você lembra de Teoria dos Conjuntos na matemática escolar, você já sabe como o Set do Python funciona! Em Python, um Set é uma coleção que é **desordenada**, **não indexada**, e que **não permite itens duplicados**.

## 2. O que são os Conjuntos em Python?
Os Sets também usam chaves `{}`, mas ao contrário dos Dicionários, eles não possuem pares "chave:valor", são apenas os valores puros separados por vírgula.

```python
# Criando um conjunto de frutas
meu_set = {"Maçã", "Banana", "Cereja"}

# Conjuntos não permitem duplicatas! O Python ignorará a segunda Maçã magicamente:
set_duplicado = {"Maçã", "Banana", "Maçã"}
print(set_duplicado) # Resultará em {'Maçã', 'Banana'}
```

## 3. Acessando Elementos
Por serem desordenados (a ordem interna dos itens embaralha), você **não pode** acessar os itens do conjunto se referindo a um índice ou uma chave.
`print(meu_set[0])` gerará um erro.

A única forma é perguntando diretamente usando o operador `in`, ou iterando num `for` loop:
```python
if "Banana" in meu_set:
    print("A banana está no conjunto!")
```
> [!TIP]
> A verificação de pertencimento (usando `in`) em Conjuntos é **muito** mais rápida e eficiente computacionalmente do que em Listas! Se você tiver milhões de dados, prefira converter listas para conjuntos caso precise fazer muitas buscas `in`.

## 4. Realizando Operações Específicas de Conjunto
A força real do Set é unir dados imitando a matemática:
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União (Une os dois conjuntos, ignorando repetições)
print(A.union(B))         # {1, 2, 3, 4, 5, 6}

# Interseção (Mantém apenas os que estão em ambos)
print(A.intersection(B))  # {3, 4}

# Diferença (Tudo que tem em A que não tem em B)
print(A.difference(B))    # {1, 2}
```

## 5. Funções Integradas e Modificação
Embora os itens que o conjunto abriga precisem ser imutáveis (como números e strings), o conjunto em si é mutável.
- `set.add(item)`: Adiciona um novo valor.
- `set.remove(item)`: Remove o valor (e gera erro se o item não existir).
- `set.discard(item)`: Remove o valor (sem gerar erro se o item já não estava lá).

## 6. Métodos de Conjunto em Python
Além de união e intersecção, funções booleanas especiais estão embutidas:
- `A.issubset(B)`: Retorna `True` se todos os itens de A também estiverem em B (A está contido em B).
- `A.issuperset(B)`: Retorna `True` se A contiver todos os itens de B.
- `A.isdisjoint(B)`: Retorna `True` se A e B não tiverem nenhum elemento em comum.

---
*Próximo Módulo:* [[8. Funções|08_Funcoes]]
