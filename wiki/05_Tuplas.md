# 5. Listas Somente Leitura: Tuplas

Vimos que as Listas são muito poderosas por serem mutáveis. Porém, em muitos casos, precisamos de estruturas que **não** podem ser alteradas acidentalmente. É aí que entram as Tuplas.

## 1. Introdução
Tuplas (Tuples) são como irmãos gêmeos das Listas. Elas guardam múltiplos itens em uma ordem definida. A grande e única diferença é que as Tuplas são **imutáveis** — depois de criadas, não é possível adicionar, alterar ou remover elementos delas.

## 2. Tuplas em Python
Uma tupla é criada ao separar itens com vírgula e envolvê-los em parênteses `()`.

```python
# Criando uma Tupla
coordenadas = (-23.5505, -46.6333)

# Uma tupla com apenas um elemento precisa de uma vírgula (senão o Python acha que é uma variável entre parênteses matemáticos)
uma_tupla = (10,)
```

## 3. Manipulando Tuplas
Você pode fatiar (slicing) e ler os itens de uma tupla exatamente da mesma forma que em uma lista.

```python
cores = ("Vermelho", "Verde", "Azul", "Amarelo")
print(cores[1])      # 'Verde'
print(cores[-1])     # 'Amarelo'
```

Mas tentar alterar falhará:
```python
cores[0] = "Roxo" # ISTO CAUSARÁ UM ERRO! TypeError: 'tuple' object does not support item assignment
```

## 4. Operações Básicas em Tuplas
Apesar da imutabilidade do conteúdo, você ainda pode usar os operadores básicos como nas strings e listas para gerar *novas* tuplas.

- Adição: `tupla1 + tupla2` une as duas, resultando em uma terceira tupla.
- Multiplicação: `tupla * 3` repete o seu conteúdo.
- Operador de Pertinência: `if "Verde" in cores:` (checa se existe).

## 5. Funções de Tupla
Como as tuplas não podem ser alteradas, elas não possuem os métodos `.append()`, `.remove()`, ou `.pop()`. Suas funções principais limitam-se à leitura:

- `tupla.count(valor)`: Conta quantas vezes um valor específico aparece dentro dela.
- `tupla.index(valor)`: Retorna a posição (índice) do primeiro elemento correspondente ao valor buscado.
- `len(tupla)`: Conta o número total de itens.

## 6. Por que Tuple?
Se Listas fazem tudo que as Tuplas fazem (e mais), por que usar Tuplas?
1. **Segurança de Dados**: Quando passamos dados constantes e críticos por todo o nosso código, não queremos correr o risco de outra função modificá-los acidentalmente (como as coordenadas geográficas em um mapa ou configurações fixas do sistema).
2. **Performance**: O Python lida com tuplas de forma um pouco mais rápida e gastando menos memória (justamente por não precisarem acomodar modificações no futuro).
3. **Chaves de Dicionário**: Diferente das Listas, as Tuplas podem ser usadas como chaves em Dicionários.

---
*Próximo Módulo:* [[6. Pares Chave-Valor|06_Pares_Chave_Valor]]
