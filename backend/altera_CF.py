import sqlite3
class Altera_CF:
    def altera_cf(self, id_cliente, NomeCliente, Endereco, Telefone, Email):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()
        """
        id_cliente = input('Digite id do cliente: ')
        NomeCliente = input('Digite o nome do cliente')
        ENDERECO = input('Digite o cpf do cliente')
        TELEFONE = input('Digite o RG do cliente')
        EMAIL =  input('Digite o RG do cliente')
        """

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE clientes
        SET nomeCliente = ?, endereco = ?, telefone = ?, email = ?
        WHERE id = ?
        """, (NomeCliente, Endereco, Telefone, Email, id_cliente))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()