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
                tipo VARCHAR(40) NOT NULL,
                metragem INTEGER NOT NULL,
                valorMetro INTEGER NOT NULL,
                dataConclusao DATE NOT NULL,
                dataContratacao DATE NOT NULL,
                valorTotal INTEGER NOT NULL,
                valorRecebido INTEGER NOT NULL,
                valorAReceber INTEGER NOT NULL,
                quantidadeParcelas INTEGER NOT NULL,
                dataParcela DATE NOT NULL
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
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nomeCliente VARCHAR(40) NOT NULL,
                nomeCliente2 VARCHAR(40),
                telefone VARCHAR(15) NOT NULL,
                telefone2 VARCHAR(15),
                email VARCHAR(40) NOT NULL,
                email2 VARCHAR(40),
                endereco VARCHAR(100) NOT NULL,
                tipoDeObra VARCHAR(50) NOT NULL
            );
            """)

        print('Tabela criada com sucesso.')
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
                valorTotal INTEGER NOT NULL,
                valorAReceber INTEGER NOT NULL,
                valorDesenhista INTEGER NOT NULL,
                valorImpostos INTEGER NOT NULL,
                valorContabilidade INTEGER NOT NULL,
                valorFuncionarios INTEGER NOT NULL,
                valorPapelaria INTEGER NOT NULL,
                valorFaxina INTEGER NOT NULL,
                outrosGastos INTEGER NOT NULL,                
                detalhesGastos VARCHAR(4000)
            );
            """)

        print('Tabela criada com sucesso.')
        # desconectando...
        conn.close()

       