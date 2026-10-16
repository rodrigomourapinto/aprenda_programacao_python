# 3. String em Python

Lidar com textos de forma eficiente é uma das maiores forças da linguagem Python. Neste módulo, dominaremos a manipulação de Strings.

## 1. Introdução
Uma "String" é essencialmente um bloco de texto. Por baixo dos panos, o Python trata a String como uma sequência imutável de caracteres, o que nos permite realizar truques muito poderosos.

## 2. Uma String
Strings em Python podem ser declaradas usando aspas simples `'Olá'`, aspas duplas `"Mundo"` ou aspas triplas `"""Texto multilinhas"""`.

```python
texto_simples = "Python é divertido"
texto_longo = """Isso permite escrever textos
em múltiplas linhas
sem quebrar o código."""
```

## 3. Fatiamento em Python (Slicing)
Como uma string é uma sequência, cada caractere tem um índice (começando no zero). O "slicing" permite fatiar e extrair pedaços do texto usando a sintaxe `[início:fim:passo]`.

```python
palavra = "Programação"
print(palavra[0])      # Retorna 'P'
print(palavra[0:5])    # Retorna 'Progr' (O índice 5 não é incluído)
print(palavra[-2:])    # Retorna 'ão' (Índices negativos começam de trás para frente)
print(palavra[::-1])   # Retorna a string invertida: 'oãçamargorP'
```

## 4. Formatação de String
Inserir variáveis dinâmicas dentro de uma string estática costumava ser chato. Hoje em Python, a forma mais moderna, rápida e recomendada de fazer isso são as **f-strings** (adicionadas no Python 3.6).

```python
nome = "Carlos"
pontos = 1500
# Basta colocar o 'f' antes das aspas e injetar as variáveis usando chaves {}
mensagem = f"Parabéns {nome}, você marcou {pontos} pontos!"
print(mensagem)
```

## 5. Modificando String
> [!IMPORTANT]
> Strings em Python são **Imutáveis**. Isso significa que, uma vez criadas na memória, elas não podem ser alteradas. Quando você usa uma função para modificar uma string, o Python na verdade devolve uma *nova* string, mantendo a original intacta.

## 6. Concatenação de Strings
Você pode juntar duas ou mais strings usando o operador de adição `+` ou multiplicar uma string usando `*`.

```python
ola = "Olá "
mundo = "Mundo!"
junto = ola + mundo     # "Olá Mundo!"
eco = "Eco! " * 3       # "Eco! Eco! Eco! "
```

## 7. Funções de String
O Python inclui métodos embutidos poderosíssimos para tratar textos sem precisar escrever códigos complexos.

- `len(texto)`: Retorna a quantidade de caracteres.
- `texto.upper()` e `texto.lower()`: Converte tudo para maiúsculas ou minúsculas.
- `texto.replace("x", "y")`: Substitui ocorrências da letra/palavra x por y.
- `texto.split(",")`: Corta o texto no separador escolhido (vírgula, espaço) e devolve uma Lista de pedaços.
- `texto.strip()`: Remove espaços em branco do começo e do final da frase.

---
*Próximo Módulo:* [[4. Listas|04_Listas]]
