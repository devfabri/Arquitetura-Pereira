import sqlite3
class Ler_CF:
    def leia_cf(self):
        conn = sqlite3.connect('cliente.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT * FROM clientes;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()