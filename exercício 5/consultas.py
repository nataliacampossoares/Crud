from conexao_criacao import get_conexao_postgres

def consultas():
    conexao = get_conexao_postgres()
    cursor = conexao.cursor()
    
    #consulta 1: todos os contatos da tabela
    cursor.execute("SELECT * FROM contato")
    contatos = cursor.fetchall()
    for contato in contatos:
        print(contato)
    print('\n')
    
    #consulta 2: contatos de uma cidade específica
    cursor.execute("SELECT nome FROM contato WHERE cidade='Rio de Janeiro'")
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)
    print('\n')
    
    #consulta 3: pessoas que nasceram antes de uma determinada data
    cursor.execute("SELECT nome FROM contato WHERE data_nasc < '09-03-2000'")
    individuos = cursor.fetchall()
    lista_individuos = []
    for individuo in individuos:
        lista_individuos.append(individuo)
    print(lista_individuos)
    
    cursor.close()
    conexao.close()
    
consultas()