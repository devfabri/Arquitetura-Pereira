import sqlite3
class Altera_CF:
    def altera_cf(self, id_cliente, NomeCliente, NomeCliente2, Telefone, Telefone2, Email, Email2, Endereco, TipoDeObra):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE clientes
        SET nomeCliente = ?, nomeCliente2 = ?, telefone = ?, telefone2 = ?, email = ?, email2 = ?, endereco = ?, tipoDeObra = ?
        WHERE id = ?
        """, (NomeCliente, NomeCliente2, Telefone, Telefone2, Email, Email2, Endereco, TipoDeObra, id_cliente))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()