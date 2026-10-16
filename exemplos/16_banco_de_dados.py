# Exemplo Teórico de Conexão MySQL (Exige o módulo mysql-connector-python instalado)
import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="minha_loja" 
    )

    cursor = conexao.cursor()

    # Inserindo
    sql_inserir = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
    valores = ("Mouse Gamer", 150.00)
    cursor.execute(sql_inserir, valores)
    conexao.commit() 

    # Buscando
    cursor.execute("SELECT * FROM produtos")
    resultado = cursor.fetchall() 

    for linha in resultado:
        print(linha) 

except Exception as e:
    print("Erro na conexão com Banco de Dados. Verifique se o MySQL está rodando.")
    print("Erro detalhado:", e)
