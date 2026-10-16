# 6. Pares Chave-Valor

Nem sempre organizar dados apenas por sua posição (índice 0, 1, 2...) faz sentido no mundo real. Para dados com significados complexos, usamos os Dicionários!

## 1. Introdução
Em Python, um Dicionário é uma estrutura que mapeia "chaves" exclusivas a "valores". É equivalente ao que outras linguagens de programação chamam de Mapas (Maps), Hash Tables ou Arrays Associativos. Imagine um dicionário da vida real: você procura uma palavra (chave) para ler o seu significado (valor).

## 2. O que é um Dicionário?
Os Dicionários são criados usando chaves `{}` (chaves no sentido de parênteses curvos) com as associações separadas por dois pontos `:`.

```python
# Criando um dicionário do perfil de um usuário
usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com",
    "is_admin": False
}
```

## 3. Manipulando Dicionários
Diferente das listas onde usamos números (índices), no dicionário nós buscamos os dados diretamente por seus nomes de chave. Os Dicionários são **mutáveis**.

```python
# Lendo um valor
print(usuario["nome"])  # 'João'

# Atualizando um valor
usuario["idade"] = 26

# Adicionando um novo par chave-valor
usuario["telefone"] = "9999-9999"

# Apagando uma chave
del usuario["is_admin"]
```

## 4. Funções de Dicionário
O Python fornece métodos embutidos para ajudar na manipulação.
- `dicionario.get("chave")`: Retorna o valor com segurança. Se a chave não existir, não causará erro, retornará `None`.
- `dicionario.keys()`: Retorna uma lista contendo apenas as chaves (`nome, idade...`).
- `dicionario.values()`: Retorna uma lista contendo apenas os valores (`João, 26...`).
- `dicionario.items()`: Retorna uma lista de tuplas contendo o par `(chave, valor)`.
- `dicionario.pop("chave")`: Remove o item especificado e devolve o valor.

## 5. Iterando sobre um dicionário
Percorrer dicionários em laços exige atenção extra, porque eles contêm tanto a chave quanto o valor. O modo mais comum é usar a função `.items()` vista acima.

```python
# Extrai as duas variáveis a cada passo do loop
for chave, valor in usuario.items():
    print(f"O(A) {chave} do usuário é {valor}.")
```

## 6. Teste de Conhecimentos
* Pratique o uso da função `.get()`! Se tentarmos ler `usuario["endereco"]` e isso não existir, o programa "quebra" (gera erro `KeyError`). Sempre prefira o método `.get()` para buscar dados incertos.

---
*Próximo Módulo:* [[7. Conjuntos|07_Conjuntos]]
