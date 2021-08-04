import sqlite3

class Novo:
    def cria(self):        
        # conectando...
        conn = sqlite3.connect('projeto.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projeto (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                tipodeprojeto VARCHAR(40) NOT NULL,
                metragem DOUBLE NOT NULL,
                valorMetro DOUBLE NOT NULL,
                dataConclusao DATE NOT NULL,
                dataContratacao DATE NOT NULL,
                valorTotal DOUBLE NOT NULL,
                valorRecebido DOUBLE NOT NULL,
                valorAReceber DOUBLE NOT NULL,
                quantidadeParcelas INTEGER NOT NULL,
                dataParcela DATE NOT NULL
            );
            """)


        print('Tabela projeto criada com sucesso.')
        # desconectando...
        conn.close()

        # conectando...
        conn = sqlite3.connect('cliente.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nomeCliente VARCHAR(40) NOT NULL,
                nomeCliente2 VARCHAR(40),
                telefone VARCHAR(15) NOT NULL,
                telefone2 VARCHAR(15),
                email VARCHAR(40) NOT NULL,
                email2 VARCHAR(40),
                endereco VARCHAR(100) NOT NULL,
                tipodecliente VARCHAR(50) NOT NULL,
                cpf VARCHAR(40)
            );
            """)

        print('Tabela cliente criada com sucesso.')
        # desconectando...
        conn.close()

        # conectando...
        conn = sqlite3.connect('financeiro.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS financeiro (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data DATETIME,
                valorAReceber DOUBLE DEFAULT 0.00,
                valorDesenhista DOUBLE DEFAULT 0.00,
                valorImpostos DOUBLE DEFAULT 0.00,
                valorContabilidade DOUBLE DEFAULT 0.00,
                valorFuncionarios DOUBLE DEFAULT 0.00,
                valorPapelaria DOUBLE DEFAULT 0.00,
                valorFaxina DOUBLE DEFAULT 0.00,
                outrosGastos DOUBLE DEFAULT 0.00,                
                detalhesGastos VARCHAR(4000),
                valorExtra DOUBLE DEFAULT 0.00                
            );
            """)

        print('Tabela financeiro criada com sucesso.')
        # desconectando...
        conn.close()

        conn = sqlite3.connect('usuario.db')
        cursor = conn.cursor()

        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                password VARCHAR(40) NOT NULL
            );
            """)

        print("Tabela usuario criada com suceso")

       