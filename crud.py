import psycopg2
from datetime import date 

def get_conexao_postgres(banco_de_dados: str, usuario: str, senha: str, host: str = "localhost", porta: int = 5432):
    conn = psycopg2.connect(
        host=host,
        database=banco_de_dados,
        user=usuario,
        password=senha,
        port=porta
    )
    return conn


def cria_tabela_contato():
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE Contato (
            ID INTEGER PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            data_nasc DATE NOT NULL,
            tel INTEGER NOT NULL,
            rua VARCHAR (50) NOT NULL,
            num_residencia INT NOT NULL,
            complemento VARCHAR (100),
            cidade VARCHAR (20) NOT NULL,
            estado VARCHAR (20) NOT NULL,
            pais VARCHAR (20) NOT NULL,
            cep INT
        );
    """)

    """contatos = [
        ,
        ('Maria Santos', '1985-03-20', 9876543210, 'Rua B', 456, 'Rio de Janeiro', 'RJ', 'Brasil', 87654321),
        ('Carlos Pereira', '1978-12-10', 5555555555, 'Rua C', 789, 'Casa', 'Belo Horizonte', 'MG', 'Brasil', 54321098),
        ('Ana Ferreira', '1995-08-25', 9999999999, 'Rua D', 101, 'Bloco 3, Ap 202', 'Porto Alegre', 'RS', 'Brasil', 98765432),
        ('Pedro Oliveira', '1982-04-05', 1111111111, 'Rua E', 222, 'Sobrado', 'Curitiba', 'PR', 'Brasil', 76543210),
        ]"""
    
    cursor.execute ('''
        INSERT INTO Contato VALUES
        (1, 'João Silva', '1990-05-15', 1234567890, 'Rua A', 123, 'São Paulo', 'SP', 'Brasil', 12345678)
    ''')


    conexao.commit()

    cursor.close()
    conexao.close()


conexao = get_conexao_postgres("banco_de_dados", "natalia", "natipedro14")
cria_tabela_contato()
