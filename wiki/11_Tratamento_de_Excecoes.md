# 11. Tratamento de Exceções

Mesmo o melhor código do mundo não está imune a erros. Se o seu programa tentar abrir um arquivo que foi apagado ou tentar dividir um número por zero, ele vai "crashar". Para evitar que o sistema inteiro congele, usamos Tratamento de Exceções.

## 1. Introdução
Quando um erro de execução ocorre (um evento inesperado que impede o código de prosseguir), o Python levanta uma "Exceção" (Exception). Se você não a capturar, o programa acaba de maneira abrupta. O tratamento de exceções intercepta essa bomba-relógio e a desarma de forma elegante.

## 2. Erros em Python
Existem os erros de *Sintaxe* (como esquecer de fechar um parêntese), que não deixam nem o código começar a rodar; e existem os erros lógicos ou de execução (Exceptions), como:
- `ZeroDivisionError`: Tentou dividir por 0.
- `FileNotFoundError`: Arquivo não encontrado.
- `ValueError`: Digitar letras quando a função esperava números inteiros (`int("Texto")`).

## 3. Tratamento de Exceções
Para lidar com esses erros, usamos blocos `try` e `except` (Tentar e Exceto). O Python "tenta" rodar o código perigoso dentro do bloco `try`. Se ele falhar, em vez de crashar a tela vermelha para o usuário, ele salta diretamente para o bloco `except` silenciosamente.

## 4. Exceções em Python
Você pode (e deve) interceptar erros específicos para poder dar respostas específicas. Capturar "todas as exceções de uma vez" é considerada uma má prática porque esconde problemas reais que você não previu.

## 5. Estrutura de Tratamento de Exceções
A estrutura completa engloba 4 palavras-chave: `try`, `except`, `else` e `finally`.

```python
try:
    # Código Perigoso!
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    
except ValueError:
    # Executa apenas se o usuário digitar letras no lugar de números
    print("Por favor, digite um número válido!")
    
except ZeroDivisionError:
    # Executa apenas se o usuário digitar 0
    print("Não é possível dividir cem por zero!")
    
else:
    # O Bloco Else só executa se o Try foi 100% SUCESSO (nenhum erro aconteceu)
    print(f"O resultado com sucesso é {resultado}")
    
finally:
    # O bloco Finally sempre executa, não importa o que aconteceu (com erro ou sem erro).
    # Muito usado para fechar banco de dados e arquivos
    print("Operação finalizada.")
```

## 6. Vamos Experimentar
A melhor forma de testar é pedir para o usuário digitar coisas proibidas em sistemas robustos.

> [!TIP]
> Tente colocar um loop infinito (`while True`) junto com o bloco de `try...except` para forçar o usuário a digitar o valor correto. Só chame o comando `break` caso o bloco seja concluído com sucesso!

---
*Próximo Módulo:* [[12. Módulos|12_Modulos]]
