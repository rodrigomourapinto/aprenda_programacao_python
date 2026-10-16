# 10. Manipulação de Arquivos

Nosso sistema de caixa do módulo anterior tinha um problema grave: toda vez que o programa fechava, o carrinho e os produtos "sumiam". Isso acontece porque as Variáveis vivem na Memória RAM (volátil).

## 1. Introdução
Para fazer dados sobreviverem ao fechamento de um programa, precisamos guardá-los permanentemente no disco rígido do computador. Faremos isso através da manipulação de arquivos de texto.

## 2. O que são os Arquivos? Por que Arquivos?
Um arquivo é uma coleção de dados nomeados e armazenados no seu computador. Aprender a interagir com eles via Python nos permite salvar recibos, ler configurações e criar "bancos de dados" simples em formato de texto `.txt` ou `.csv`.

## 3. Abrindo os Arquivos
No Python, usamos a função integrada `open()` para criar um objeto de arquivo. A função requer dois argumentos cruciais: o nome/caminho do arquivo e o **Modo de Abertura**.
- `"r"` (Read): Ler o arquivo.
- `"w"` (Write): Escrever (Apaga tudo e reescreve).
- `"a"` (Append): Anexar (Escreve no final sem apagar o que já existia).

```python
arquivo = open("recibo.txt", "w")
```

## 4. Lendo dados de arquivos
Para ler um arquivo existente, você o abre no modo `"r"`. O arquivo deve existir para que não ocorra um erro.

```python
# Abre o arquivo em modo leitura
with open("meus_dados.txt", "r") as arquivo:
    conteudo = arquivo.read()       # Lê o arquivo inteiro como uma String gigante
    print(conteudo)
    
# Dica: O bloco 'with open()' fecha o arquivo automaticamente para você ao final!
```
Você também pode ler as linhas individualmente usando `.readlines()` (retorna uma Lista de linhas) ou usando um laço `for linha in arquivo:`.

## 5. Writing to a File
Ao usar o modo `"w"`, se o arquivo não existir, o Python o criará para você. Tome cuidado: se ele existir, o modo `"w"` vai esmagar o conteúdo anterior. Para manter o passado e adicionar ao final, use o modo `"a"`.

```python
# Modo Write
with open("log.txt", "w") as f:
    f.write("Primeira linha de log.\n")

# Modo Append (Adiciona na linha de baixo)
with open("log.txt", "a") as f:
    f.write("Segunda linha adicionada depois!\n")
```

## 6. Fechando um Arquivo
Sempre que você abre um arquivo com `open()`, o Sistema Operacional trava aquele arquivo para o Python. É crucial fechá-lo depois com a função `arquivo.close()`. 
A prática mais recomendada, como vimos acima, é usar o *context manager* `with open() as f:`, pois ele executa o `close()` automaticamente, mesmo se o programa der um erro fatal no meio do processo!

---
*Próximo Módulo:* [[11. Tratamento de Exceções|11_Tratamento_de_Excecoes]]
