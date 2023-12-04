from conexao_criacao import get_conexao_postgres

def atualizar_contato(conexao, id, novo_telefone, novo_endereco):
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Contato WHERE ID = %s", (id))
    contato = cursor.fetchone()

    if contato:
        cursor.execute("UPDATE Contato SET tel = %s, rua = %s WHERE ID = %s",
                       (novo_telefone, novo_endereco, id))
        conexao.commit()
        print("Contato atualizado com sucesso.")
    else:
        print(f"Contato com ID {id} não encontrado.")

    cursor.close()
    
def excluir_contato_telefone(conexao, telefone):
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM Contato WHERE tel = %s", (telefone,))
    contato = cursor.fetchone()
    
    if contato:
        cursor.execute("DELETE FROM Contato WHERE tel = %s",
                       (telefone,))
        conexao.commit()
        print("Contato excluído com sucesso")
    else:
        print(f"Contato com telefone {telefone} não encontrado.")

def excluir_contato_nome(conexao, nome):
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM Contato WHERE nome = %s", (nome,))
    contato = cursor.fetchone()
    
    if contato:
        cursor.execute("DELETE FROM Contato WHERE nome = %s",
                       (nome,))
        conexao.commit()
        print("Contato excluído com sucesso")
    else:
        print(f"Contato com nome {nome} não encontrado.")
        
conexao = get_conexao_postgres()
atualizar_contato(conexao, 4, 987654321, 'Nova Rua XYZ, 456')
excluir_contato_telefone(conexao, 9876543210)
excluir_contato_nome(conexao, "João Silva")
conexao.close()
