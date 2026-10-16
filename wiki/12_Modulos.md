# 12. Módulos

Escrever um código inteiro de 10.000 linhas em um único arquivo `.py` é insano de manter. Os Módulos existem para organizarmos nossos sistemas.

## 1. Introdução
Em um ambiente profissional, softwares são organizados em diversos arquivos separados (por funcionalidade). Esses arquivos individuais que abrigam conjuntos de funções são chamados de **Módulos**. 

## 2. O que são módulos?
De forma simples, qualquer arquivo com a extensão `.py` contendo código executável, classes ou funções é um módulo. Quando você precisa utilizar uma função contida nele a partir de outro arquivo diferente, você deve importá-lo.

## 3. Tipos de módulos
- **Módulos Embutidos (Built-ins):** Vem por padrão na instalação original do Python (Ex: `math`, `random`, `datetime`, `os`).
- **Módulos Externos:** Módulos feitos por outros programadores que não vêm com o Python. Precisam ser instalados usando a ferramenta `pip` (Ex: `pandas`, `requests`, `numpy`).
- **Módulos Personalizados:** Arquivos `.py` criados por você mesmo na mesma pasta do seu projeto.

## 4. Como usar um módulo?
Para usar um módulo, seja ele embutido ou personalizado, usamos a declaração `import`.

```python
# Importa o módulo inteiro
import math
print(math.sqrt(25)) # Calcula a raiz quadrada acessando o módulo

# Importa apenas uma função específica (evita carregar a memória inteira do módulo)
from datetime import datetime
agora = datetime.now()

# Importando e dando um "apelido" (alias)
import pandas as pd
```

## 5. Alguns módulos embutidos
O poder do Python está nas baterias inclusas.
- **math**: Contém trigonometria, constantes (`math.pi`), e matemática avançada.
- **random**: Gera escolhas aleatórias. Muito usado em sorteios e estatísticas:
  ```python
  import random
  vencedor = random.choice(["Ana", "Carlos", "Bruno"])
  ```
- **time**: Utilizado para manipular tempos (por exemplo, fazer o programa pausar com `time.sleep(5)`).

## 6. Trabalhando com módulos personalizados
Se você criar um arquivo chamado `meus_calculos.py` com a seguinte função nele:
```python
# dentro do arquivo meus_calculos.py
def dobro(n):
    return n * 2
```

No seu arquivo principal, chamado `main.py` que está na mesma pasta, você fará assim:
```python
# dentro do arquivo main.py
import meus_calculos

print("O dobro de 5 é", meus_calculos.dobro(5))
```

Assim, construímos softwares organizados e modulares!

---
*Próximo Módulo:* [[13. Programação Orientada a Objetos|13_Programacao_Orientada_a_Objetos]]
