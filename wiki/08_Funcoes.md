# 8. Funções

Reescrever a mesma lógica em partes diferentes do seu sistema é a receita para gerar dores de cabeça a longo prazo. É para solucionar isso que as funções nasceram!

## 1. Introdução
Uma Função é um bloco de código que só roda quando é expressamente "chamado". Você dá um nome àquele pedaço de código e pode invocá-lo onde precisar, quantas vezes precisar.

## 2. O que é uma Função?
Nos módulos anteriores, você já usou várias funções nativas (built-ins) do Python, como `print()`, `input()`, e `len()`. Agora, vamos criar as nossas próprias.

## 3. Compreendendo a Estrutura
Em Python, as funções são declaradas utilizando a palavra-chave `def` (de *define*). Após o nome da função, abrimos e fechamos parênteses e usamos os dois pontos `:`. O código pertencente à função deve estar indentado na linha abaixo.

```python
def dar_boas_vindas():
    print("Olá, bem-vindo ao nosso sistema!")
```

## 4. Definindo uma Função
Uma função declarada não executa seu código imediatamente. Você precisa chamá-la.

```python
dar_boas_vindas()  # O programa exibirá a mensagem agora.
```

Uma função geralmente devolve um valor de volta para o sistema usando a palavra `return`.
```python
def somar_simples():
    resultado = 2 + 2
    return resultado

print(somar_simples()) # Vai imprimir 4
```

## 5. Argumentos de Função
Funções tornam-se extremamente úteis quando recebem "Argumentos" (ou parâmetros). Você passa dados diferentes e a função age com base nesses dados.

```python
# A função pede dois números (a e b)
def calcular_area(base, altura):
    area = base * altura
    return area

# Chamando a função várias vezes com dados distintos!
terreno_a = calcular_area(10, 5)  # Retornará 50
terreno_b = calcular_area(20, 2)  # Retornará 40
```
Você pode criar argumentos com um "valor padrão", o que os torna opcionais: `def saudacao(nome="Visitante"):`.

## 6. Lambda em Python
Às vezes você quer uma função pequena, de uma linha só, que você vai usar só temporariamente (muito comum em Ciência de Dados ou mapeamento de listas). Nesses casos, evitamos escrever a burocracia do `def` e usamos as "Funções Lambda", ou funções anônimas.

```python
# Sintaxe: lambda argumentos : expressão

# Função normal:
def dobrar_normal(x):
    return x * 2

# Função Lambda equivalente:
dobrar_lambda = lambda x : x * 2

print(dobrar_lambda(5)) # Imprime 10
```

---
*Próximo Módulo:* [[9. Projeto Um - Caixa|09_Projeto_Um_Caixa]]
