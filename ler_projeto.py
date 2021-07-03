import sqlite3
class Ler_Projeto:
    def leia_proj(self):
        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT * FROM projeto;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()