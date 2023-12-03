import psycopg2
from datetime import date

def get_conexao_postgres (banco_de_dados: str = 'contatos', usuario: str = 'natalia', senha: str = 'natipedro14', host: str = 'localhost', porta: int = 5432):
    conn = psycopg2.connect(
        host = host,
        database = banco_de_dados,
        user = usuario,
        password = senha,
        port = porta
    )
    return conn

def cria_tabela_contato(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Contato;
        
        CREATE TABLE Contato (
            ID INTEGER PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            data_nasc DATE NOT NULL,
            tel BIGINT NOT NULL,
            rua VARCHAR (50) NOT NULL,
            num_residencia INT NOT NULL,
            cidade VARCHAR (20) NOT NULL,
            estado VARCHAR (20) NOT NULL,
            pais VARCHAR (20) NOT NULL,
            cep INT
        );
    """)
    
    cursor.execute("""
        INSERT INTO Contato VALUES
        (1, 'João Silva', '1990-05-15', 1234567890, 'Rua A', 123, 'São Paulo', 'SP', 'Brasil', 12345678),
        (2, 'Maria Santos', '1985-03-20', 9876543210, 'Rua B', 456, 'Rio de Janeiro', 'RJ', 'Brasil', 87654321),
        (3, 'Carlos Pereira', '1978-12-10', 5555555555, 'Rua C', 789, 'Belo Horizonte', 'MG', 'Brasil', 54321098),
        (4, 'Ana Ferreira', '1995-08-25', 9999999999, 'Rua D', 101, 'Porto Alegre', 'RS', 'Brasil', 98765432),
        (5, 'Pedro Oliveira', '1982-04-05', 1111111111, 'Rua E', 222, 'Curitiba', 'PR', 'Brasil', 76543210)
        """)
    
    conexao.commit()
    cursor.close()
    conexao.close()
    
conexao = get_conexao_postgres()
cria_tabela_contato(conexao)
    