import sqlite3

# Conectar ao banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Cadastrar livro
def insert_book(titulo, autor, genero):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, genero) VALUES (?, ?, ?)", (titulo, autor, genero))
    conn.commit()
    conn.close()

# Inserir usuário
def insert_user(nome, sobrenome, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, telefone) VALUES (?, ?, ?)", (nome, sobrenome, telefone))
    conn.commit()
    conn.close()

# Exibir usuários
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Exibir livros
def get_books():
    conn = connect()
    c = conn.cursor()  # Declaração do cursor
    c.execute("SELECT * FROM livros")
    books = c.fetchall()
    conn.close()
    return books

# Realizar empréstimo
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", 
                 (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Exibir livros emprestados
def get_books_on_loan():
    conn = connect()
    c = conn.cursor()  # Declaração do cursor
    result = c.execute("""
        SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.id, emprestimos.data_emprestimo, emprestimos.data_devolucao
        FROM livros
        INNER JOIN emprestimos ON livros.id = emprestimos.id_livro
        INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario
        WHERE emprestimos.data_devolucao IS NULL
    """).fetchall()  # Corrigido fetchfall para fetchall
    conn.close()
    return result

# Atualizar data de devolução do empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))  # Corrigido data_devpolucao para data_devolucao
    conn.commit()
    conn.close()
