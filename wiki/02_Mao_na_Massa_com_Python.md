# 2. Mão na Massa com Python

Após entender os fundamentos absolutos, é hora de sujar as mãos e escrever programas que interagem com o usuário, tomam decisões lógicas e executam tarefas repetitivas automaticamente.

## 1. Introdução
Neste módulo, vamos explorar a base do fluxo de controle em Python. Programas deixam de ser apenas cálculos estáticos e passam a ser dinâmicos.

## 2. Entrada/Saída
Qualquer programa útil precisa receber dados (entrada) e devolver resultados (saída).
- **Entrada (`input`)**: Permite que o programa pause e espere o usuário digitar algo no teclado. O retorno é sempre uma string.
- **Saída (`print`)**: Exibe dados na tela do console.

```python
# Solicitando o nome do usuário
nome = input("Qual é o seu nome? ")
# Exibindo uma saudação
print("Olá,", nome)
```

## 3. Comentários em Python
Comentários são anotações no código ignoradas pelo interpretador. Servem para explicar o que um bloco complexo faz ou para desativar temporariamente linhas de código.
Em Python, usa-se o símbolo da hashtag `#` para comentários de linha.

```python
# Isto é um comentário e não será executado
x = 5  # Você pode colocar comentários após instruções na mesma linha
```

## 4. Números em Python
Já vimos que Python suporta `int` (inteiros) e `float` (decimais). Além disso, ele gerencia números extremamente grandes automaticamente sem estourar o limite de memória da variável (o que ocorre em Java e C). O módulo embutido `math` permite operações avançadas como raízes quadradas e trigonometria.

## 5. Operadores em Python
Os operadores são símbolos que realizam computações.
- **Aritméticos:** `+` (adição), `-` (subtração), `*` (multiplicação), `/` (divisão flutuante), `//` (divisão inteira), `%` (módulo/resto), `**` (exponenciação).
- **Comparação:** `==` (igual a), `!=` (diferente de), `>` (maior que), `<` (menor que), `>=` (maior ou igual a), `<=` (menor ou igual a). Resultam sempre em `True` ou `False`.
- **Lógicos:** `and` (e), `or` (ou), `not` (não). Combinam múltiplas condições.

## 6. Tomada de Decisão
Estruturas condicionais (`if`, `elif`, `else`) permitem que o código tome caminhos diferentes baseados em testes lógicos.

```python
idade = int(input("Qual sua idade? "))

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos.")
else:
    print("Você é maior de idade.")
```

## 7. Laços em Python
Muitas vezes, precisamos repetir o mesmo bloco de código dezenas ou milhares de vezes. Laços (loops) automatizam essa repetição enquanto uma condição for verdadeira.

## 8. Laço for vs while
- **`while` (Enquanto):** Repete o bloco *enquanto* a condição declarada for verdadeira. Ideal para quando não sabemos exatamente quantas vezes o loop precisa rodar.
- **`for` (Para):** Repete iterando sobre uma sequência (como listas, strings, ou a função `range`). É ideal para iterar uma quantidade conhecida de vezes.

```python
# Exemplo while
contador = 0
while contador < 3:
    print("Contagem:", contador)
    contador += 1  # Evita o loop infinito

# Exemplo for
for i in range(3):
    print("Iteração número:", i)
```

## 9. Controle de Laço
Existem duas palavras-chave cruciais para ter mais controle sobre loops em andamento:
- `break`: Sai do loop imediatamente, ignorando qualquer condição ou iterações restantes.
- `continue`: Pula o restante do bloco de código atual e avança para a próxima iteração do loop.

---
*Próximo Módulo:* [[3. String em Python|03_String_em_Python]]
