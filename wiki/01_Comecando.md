# 1. Começando

Bem-vindo ao primeiro módulo do curso de Python! Aqui começamos a entender o que torna essa linguagem de programação tão popular e amada por desenvolvedores em todo o mundo.

## 1. Introdução
A programação é a arte de instruir um computador para realizar tarefas específicas. Python, criado por Guido van Rossum e lançado em 1991, é uma das portas de entrada mais amigáveis e poderosas nesse universo. 

## 2. O que é Python?
Python é uma linguagem de programação de **alto nível**, **interpretada** e orientada a objetos. "Alto nível" significa que ela se aproxima da linguagem humana, tornando o código extremamente legível (semelhante ao idioma inglês). Por ser "interpretada", o código Python não precisa ser compilado (transformado em linguagem de máquina antes de rodar); o interpretador Python o executa diretamente linha por linha.

## 3. Por que Python?
A ascensão do Python é justificada por vários fatores:
- **Simplicidade e Legibilidade:** A sintaxe limpa diminui a curva de aprendizado e reduz custos de manutenção de software.
- **Ecossistema:** Possui uma vasta biblioteca padrão (baterias inclusas) para tarefas como conexão web, regex, e sistemas operacionais.
- **Versatilidade:** É a principal linguagem hoje para Ciência de Dados (Data Science), Inteligência Artificial (IA), Automação e Desenvolvimento Web (Django/Flask).
- **Comunidade:** Uma comunidade global gigantesca significa que qualquer dúvida ou erro que você encontrar já foi resolvido por alguém na internet.

## 4. Sintaxe do Python
Diferente de linguagens como C++ ou Java, que usam chaves `{}` para definir blocos de código e ponto e vírgula `;` ao final das instruções, o Python usa **indentação** (espaços) estrita para identificar onde uma estrutura de código começa e termina.

```python
# Exemplo clássico de Sintaxe e Indentação
if 5 > 2:
    print("Cinco é maior que dois!") # Esta linha faz parte do bloco 'if' devido à indentação
```

## 5. Variáveis em Python
As variáveis atuam como "caixas" de armazenamento onde guardamos dados durante a execução do programa. Em Python, não é necessário declarar o tipo da variável antes de usá-la; ele descobre dinamicamente.

```python
nome = "Maria"       # Cria uma variável contendo um texto (String)
idade = 30           # Cria uma variável contendo um número inteiro (Integer)
altura = 1.75        # Cria uma variável contendo um número decimal (Float)
programadora = True  # Cria uma variável contendo um estado verdadeiro/falso (Booleano)

print(nome, "tem", idade, "anos.")
```

## 6. Tipos de Dados
Tudo em Python é um objeto e possui um tipo. Os mais fundamentais abordados neste módulo são:
- `int`: Números inteiros (ex: `10`, `-5`)
- `float`: Números de ponto flutuante (decimais) (ex: `3.14`)
- `str`: Strings (sequências de caracteres) (ex: `"Olá Mundo"`)
- `bool`: Valores booleanos lógicos (`True` ou `False`)

> [!TIP]
> Você pode usar a função `type()` embutida no Python para descobrir qual é o tipo de dado armazenado em qualquer variável: `print(type(idade))` retornará `<class 'int'>`.

---
*Próximo Módulo:* [[2. Mão na Massa com Python|02_Mao_na_Massa_com_Python]]
