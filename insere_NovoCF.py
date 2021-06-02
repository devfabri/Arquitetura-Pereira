import sqlite3
class Novo_CF:
    def insere_Novo_CF(self,NomeCliente, Endereco, Telefone, Email):
        """
        NomeCliente = input('Digite o nome do cliente')
        CPF = input('Digite o cpf do cliente')
        RG = input('Digite o RG do cliente')
        """

        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO clientes (nomeCliente, endereco, telefone, email)
        VALUES (?,?,?,?)
        """, (NomeCliente, Endereco, Telefone, Email))

        conn.commit()

        conn.close()

        print('Dados inseridos com sucesso.')