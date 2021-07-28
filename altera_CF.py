import sqlite3
class Altera_CF:
    def altera_cf(self, id_cliente, NomeCliente, NomeCliente2, Telefone, Telefone2, Email, Email2, Endereco, Tipodecliente):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE cliente
        SET nomeCliente = ?, nomeCliente2 = ?, telefone = ?, telefone2 = ?, email = ?, email2 = ?, endereco = ?, tipodecliente = ?
        WHERE id = ?
        """, (NomeCliente, NomeCliente2, Telefone, Telefone2, Email, Email2, Endereco, Tipodecliente, id_cliente))

        conn.commit()

        print('Dados do client atualizados com sucesso.')

        conn.close()