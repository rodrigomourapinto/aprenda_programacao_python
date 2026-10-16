# 4. Listas

Um único texto ou um único número geralmente não são suficientes para um programa avançado. Freqüentemente, precisamos lidar com coleções de dezenas ou centenas de dados (como listas de usuários, resultados de buscas, ou preços de produtos). 

## 1. Introdução
As Listas são as estruturas de dados mais versáteis e utilizadas em Python. Elas permitem agrupar múltiplos itens em uma única variável. Diferente de Arrays em outras linguagens, as Listas no Python não têm tamanho fixo e podem misturar tipos de dados diferentes.

## 2. Lista em Python
Uma Lista é criada inserindo os itens separados por vírgula dentro de colchetes `[]`.

```python
# Uma lista vazia
minha_lista = []

# Uma lista com números
numeros = [1, 2, 3, 4, 5]

# Uma lista mista
mista = ["Texto", 42, 3.14, True, [1, 2]] # Sim, uma lista pode conter outra lista!
```

## 3. Manipulando Listas
Assim como as Strings, Listas são ordenadas e baseadas em índices (começando por 0). E a boa notícia: as regras de *Slicing* (fatiamento) que você aprendeu com Strings funcionam da exata mesma forma com Listas!

```python
frutas = ["Maçã", "Banana", "Cereja", "Laranja", "Kiwi"]
print(frutas[1])     # Retorna 'Banana'
print(frutas[1:3])   # Retorna ['Banana', 'Cereja']
```

## 4. Operações Básicas em Lista
Diferente das Strings, **Listas são Mutáveis**. Você pode alterar itens, adicionar novos, e remover itens em qualquer posição do seu ciclo de vida.

```python
# Alterando um item
frutas[0] = "Abacaxi" # A lista agora começa com Abacaxi

# Verificando se existe na lista (Retorna Booleano)
tem_banana = "Banana" in frutas 
```

## 5. Iterando sobre a Lista
Como uma lista contém múltiplos valores, a forma mais segura de interagir com cada valor individualmente é usando um Laço `for`.

```python
# Para cada item dentro da lista de frutas:
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
```

## 6. Funções de Lista
O Python vem recheado com métodos fantásticos para ajudar a manipular listas sem esforço.
- `lista.append(item)`: Adiciona o item ao final da lista.
- `lista.insert(indice, item)`: Insere o item na posição especificada, empurrando o resto para frente.
- `lista.pop()`: Remove e retorna o último elemento (ou o índice especificado).
- `lista.remove(item)`: Procura o valor exato na lista e o deleta (apenas a primeira ocorrência).
- `lista.sort()`: Ordena a lista em ordem crescente/alfabética (ou decrescente se usar `reverse=True`).
- `len(lista)`: Conta quantos elementos existem na lista total.

---
*Próximo Módulo:* [[5. Tuplas|05_Tuplas]]
