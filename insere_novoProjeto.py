import sqlite3
from financeiro import FinanceiroController

class Novo_Projeto(FinanceiroController):
    def insere_Novo_Projeto(self, Tipodeprojeto, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela):

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO projeto (tipodeprojeto, metragem, valorMetro, dataConclusao, dataContratacao, valorTotal, valorRecebido, valorAReceber, quantidadeParcelas, dataParcela)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, (Tipodeprojeto, Metragem, ValorMetro, DataConclusao, DataContratacao, ValorTotal, ValorRecebido, ValorAReceber, QuantidadeParcelas, DataParcela))

        conn.commit()

        conn.close()

        conn = sqlite3.connect('projeto.db')
        cursor = conn.cursor()

        cursor.execute(""" SELECT id FROM projeto WHERE id=(SELECT max(id) FROM projeto) """)
        id = cursor.fetchone()[0]


        print('Dados inseridos em -projeto- com sucesso.')

        self.dividaProjeto(ValorAReceber, id)
