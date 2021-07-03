import sqlite3
class Ler_Gastos:
    def leia_gastos(self):
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT * FROM financeiro;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()