# 19. Preparação para Entrevista de Python

Parabéns por dominar a base da linguagem Python! Se o seu objetivo for atuar no mercado de trabalho profissionalmente, você fatalmente enfrentará entrevistas técnicas. Abaixo está o resumo dos tópicos fundamentais exigidos em processos seletivos.

## 1. Fundamentos de Python
Você precisará responder na ponta da língua as teorias por trás das ferramentas que usou.
- **Diferença entre Compilada e Interpretada:** Python é interpretada, roda linha a linha através do CPython em tempo de execução.
- **Tipagem Dinâmica:** Você não precisa declarar tipos (`int`, `str`). O Python infere em tempo de execução. Em contrapartida, é mais lenta que linguagens de tipagem estática (como C ou Java).
- **Gerenciamento de Memória:** O Python tem um *Garbage Collector* automático que descarta variáveis não utilizadas da RAM.

## 2. Núcleo do Python (Tipos de Dados)
Entenda as diferenças vitais entre as estruturas.
- **Mutabilidade:** Listas, Sets e Dicionários são mutáveis. Strings e Tuplas são **imutáveis**.
- **O que é um Dicionário por baixo dos panos?** Eles usam Tabelas Hash (Hash Maps). Isso significa que as buscas pelas chaves são super-rápidas (Tempo O(1)), diferente das Listas.

## 3. Python Intermediário
Recursos que diferenciam iniciantes de programadores proficientes.
- **List Comprehensions:** A forma pythônica de criar listas em uma linha. Ex: `pares = [x for x in range(10) if x % 2 == 0]`
- **Decorators (Decoradores):** Funções que modificam o comportamento de outras funções, utilizando o símbolo `@`.
- **Tratamento de Exceções:** Saber justificar por que usar `try/except` ao invés de centenas de `if/elses`.

## 4. Conceitos Avançados de Python
Ferramentas de arquitetura e performance.
- **Generators & Yield:** Semelhante a uma função `return`, mas o `yield` pausa a função e cospe um valor por vez, poupando a memória RAM quando lidamos com milhões de registros simultâneos.
- **Multithreading e GIL (Global Interpreter Lock):** Esteja preparado para a pergunta fatal: "Por que as threads no Python não rodam 100% em paralelo real por causa do GIL?"

## 5. Python OOP
Você será intensamente testado nos pilares da Orientação a Objetos.
- **Encapsulamento, Herança e Polimorfismo:** Entenda o conceito de cada um e como aplicar na prática.
- **Métodos Dunder (Magic Methods):** São aqueles métodos com dois underlines `__`. O mais famoso é o `__init__`, mas saiba da existência do `__str__` ou `__len__`.
- Diferença entre um *Atributo de Classe* (compartilhado por todos os objetos) e um *Atributo de Instância* (único de cada objeto, vinculado com o `self`).

---
*Próximo Módulo:* [[20. Essenciais de IA para Programadores|20_Essenciais_IA_Programadores]]
