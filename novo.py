import sqlite3

class Novo:
    def cria(self):        
        # conectando...
        conn = sqlite3.connect('projeto.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tipo INTEGER NOT NULL,
                metragem INTEGER NOT NULL,
                dataConclusao DATE NOT NULL,
                etapa VARCHAR(40) NOT NULL,
                nomeCliente VARCHAR(40) NOT NULL,
                dataContratacao DATE NOT NULL,
                telefone VARCHAR(11) NOT NULL,
                vt INTEGER NOT NULL,
                va INTEGER NOT NULL,
                vp INTEGER NOT NULL,
                dp INTEGER NOT NULL,
                qp INTEGER NOT NULL,
                vm INTEGER NOT NULL,
                vmo VARCHAR(400) NOT NULL
            );
            """)


        print('Tabela criada com sucesso.')
        # desconectando...
        conn.close()

        # conectando...
        conn = sqlite3.connect('cliente.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nomeCliente VARCHAR(40) NOT NULL,
                endereco VARCHAR(40) NOT NULL,
                telefone VARCHAR(40) NOT NULL,
                email VARCHAR(40) NOT NULL

            );
            """)

        print('Tabela criada com sucesso.')
        # desconectando...
        conn.close()

       