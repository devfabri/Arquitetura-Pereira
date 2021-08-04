import sqlite3
class Novo_BD:
    def cria_BD(self):
        conn = sqlite3.connect('projeto.db')
        conn.close()

        conn = sqlite3.connect('cliente.db')
        conn.close()

        conn = sqlite3.connect('financeiro.db')
        conn.close()

        conn = sqlite3.connect('usuario.db')
        conn.close()
