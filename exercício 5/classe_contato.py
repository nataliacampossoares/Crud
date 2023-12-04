import psycopg2
from conexao_criacao import get_conexao_postgres

class Contato:
    def __init__(self, id, nome, data_nasc, tel, rua, num_residencia, cidade, estado, pais, cep):
        self.id = id
        self.nome = nome
        self.data_nasc = data_nasc
        self.tel = tel
        self.rua = rua
        self.num_residencia = num_residencia
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.cep = cep

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Data de Nascimento: {self.data_nasc}, Telefone: {self.tel}, Endereço: {self.rua}, {self.num_residencia}, {self.cidade}, {self.estado}, {self.pais}, CEP: {self.cep}"


# mapeando os resultados das consultas para objetos
conexao = get_conexao_postgres()
cursor = conexao.cursor()

def mapear_resultados(resultados):
    contatos = []
    for resultado in resultados:
        contato = Contato(*resultado)
        contatos.append(contato)
    return contatos

# consulta 1: todos os contatos da tabela
cursor.execute("SELECT * FROM contato")
resultados_consulta_1 = cursor.fetchall()
contatos_consulta_1 = mapear_resultados(resultados_consulta_1)

# consulta 2: contatos de uma cidade específica
cursor.execute("SELECT * FROM contato WHERE cidade='Rio de Janeiro'")
resultados_consulta_2 = cursor.fetchall()
contatos_consulta_2 = mapear_resultados(resultados_consulta_2)

# consulta 3: pessoas que nasceram antes de uma determinada data
cursor.execute("SELECT * FROM contato WHERE data_nasc < '1986-03-09'")
resultados_consulta_3 = cursor.fetchall()
contatos_consulta_3 = mapear_resultados(resultados_consulta_3)

# exibindo as infos
for contato in contatos_consulta_1:
   print(contato)
print('\n')

for contato in contatos_consulta_2:
    print(contato)
print('\n')

for contato in contatos_consulta_3:
   print(contato)
