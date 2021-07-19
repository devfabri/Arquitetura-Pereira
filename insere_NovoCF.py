import sqlite3
class Novo_CF:
    def insere_Novo_CF(self,NomeCliente, NomeCliente2, Telefone, Telefone2, Email, Email2, Endereco, Tipodecliente):

        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO cliente (nomeCliente, nomeCliente2, telefone, telefone2, email, email2, endereco, tipodecliente)
        VALUES (?,?,?,?,?,?,?,?)
        """, (NomeCliente, NomeCliente2, Telefone, Telefone2, Email, Email2, Endereco, Tipodecliente))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')