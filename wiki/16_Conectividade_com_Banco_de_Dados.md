# 16. Conectividade com Banco de Dados

Salvar dados em arquivos `.txt` (como vimos no Módulo 10) é útil para coisas pequenas. Mas imagine um site inteiro guardando dados de usuários em um Bloco de Notas: seria um caos de lentidão e riscos. É aqui que entram os Bancos de Dados!

## 1. Introdução
Bancos de Dados Relacionais armazenam informações em tabelas de forma estruturada. Eles garantem pesquisa rápida, segurança e integridade de gigabytes de dados.

## 2. SQL e MySQL
A linguagem universal para conversar com bancos relacionais se chama SQL (Structured Query Language). Um dos Sistemas Gerenciadores de Banco de Dados mais famosos e gratuitos do mundo é o **MySQL** (agora sob a tutela da Oracle).

## 3. Instalando o MySQL
1. Você precisa de um servidor MySQL rodando na sua máquina. A forma mais fácil é instalando um pacote como o **XAMPP** ou o MySQL Installer.
2. Para o Python conversar com o MySQL, instale a biblioteca de conexão oficial abrindo o terminal e digitando:
   `pip install mysql-connector-python`

## 4. Fundamentos do MySQL
A estrutura no banco é como o Excel: 
- Você cria um Banco de Dados (A planilha geral)
- Nele, você cria Tabelas (As abas da planilha, ex: "Usuários", "Produtos")
- Cada tabela tem Colunas (Os atributos, ex: "Nome", "Idade")

## 5. Fundamentos do MySQL - Continuado
Comandos básicos de SQL:
- `CREATE TABLE`: Cria a tabela e suas colunas.
- `SELECT`: Busca dados da tabela.
- `INSERT INTO`: Insere uma nova linha de dados.
- `UPDATE`: Atualiza dados já existentes.
- `DELETE`: Apaga linhas.

## 6. Conexão com o Banco de Dados
No Python, usamos a biblioteca instalada para estabelecer o canal de comunicação usando Usuário e Senha (geralmente `root` e senha vazia para servidores locais como XAMPP).

```python
import mysql.connector

# Criando a ponte
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", # Senha do seu banco local
    database="minha_loja" # Opcional na primeira conexão se o banco não existe
)

# Criando o 'cursor' (o mensageiro que envia nossos comandos SQL para o banco)
cursor = conexao.cursor()
```

## 7. Criando Banco de Dados e Tabelas
Usando o `cursor.execute()`, mandamos SQL nativo.

```python
# Criar o banco
cursor.execute("CREATE DATABASE se_nao_existe minha_loja")

# Mudar para o banco criado
cursor.execute("USE minha_loja")

# Criar a tabela de produtos
comando_sql = """
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    preco FLOAT
)
"""
cursor.execute(comando_sql)
```

## 8. Inserir e Buscar Dados
Diferente de consultas de leitura, qualquer alteração que modifique dados (Insert, Update, Delete) precisa ser **confirmada** em definitivo chamando o comando `conexao.commit()`.

```python
# Inserindo
sql_inserir = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
valores = ("Mouse Gamer", 150.00)
cursor.execute(sql_inserir, valores)
conexao.commit()  # Confirmação vital!

# Buscando (Lendo)
cursor.execute("SELECT * FROM produtos")
resultado = cursor.fetchall() # Traz todas as linhas da tabela

for linha in resultado:
    print(linha) # Imprime a tupla (id, nome, preco)
```

## 9. Teste
* Tente sempre utilizar `%s` nos seus comandos em vez de interpolar com f-strings ou `.format()`. Isso evita a perigosíssima falha de segurança chamada de "SQL Injection", onde usuários mal intencionados deletam o seu banco injetando comandos em campos de texto. O conector gerencia o `%s` com segurança nativa.

---
*Próximo Módulo:* [[17. GUI|17_GUI]]
