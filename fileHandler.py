import sqlite3

def conectar():
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    conn, cursor = conectar()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        score INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def inserir_score(nome, score):
    conn, cursor = conectar()
    cursor.execute("INSERT INTO scores (nome, score) VALUES (?, ?)", (nome, score))
    conn.commit()
    conn.close()

def listar_scores():
    conn, cursor = conectar()
    cursor.execute("SELECT nome, score FROM scores ORDER BY score DESC")
    scores = cursor.fetchall()
    conn.close()
    return scores

def abrir_palavras():
    with open('palavras.txt', 'r') as f:
        return [linha.strip() for linha in f.readlines()]

# Inicializando o banco de dados e criando a tabela, se necessário
criar_tabela()
